import requests
from bs4 import BeautifulSoup


class Http:

    @staticmethod
    def get_text(url: str, encoding=None) -> str:
        req = requests.get(url)

        # 인코딩 적용
        if encoding != None:
            req.encoding = encoding

        if req.status_code == 200:
            return req.text
        else:
            return req.status_code

class Crawling:

    @staticmethod
    def get_text_HwanGyeongnyuseu():
        """ 환경일보 """
        URL = "https://www.hkbs.co.kr/news/articleList.html?sc_section_code=S1N1"
        return Http.get_text(URL)

    @staticmethod
    def get_text_HanGyeore():
        """ 한겨레 """
        URL = "https://www.hani.co.kr/arti/society/environment/home01.html"
        return Http.get_text(URL)

    @staticmethod
    def get_text_HwanGyeongbeopryul():
        """ 환경 법률 신문 """
        URL = "http://www.ecolaw.co.kr/news/articleList.html?sc_sub_section_code=S2N75&view_type=sm"
        return Http.get_text(URL, encoding="EUC-KR") # EUC-KR < 한글 안깨짐

    @staticmethod
    def get_text_HwanGyeongisyu():
        """ 환경 이슈 신문 """
        URL = "http://www.hkisnews.com/sub.html?section=sc1"
        return Http.get_text(URL, encoding="UTF-8") # UTF-8 < 한글 안깨짐

class Articles:

    @staticmethod
    def get_HwanGyeongnyuseu():
        """ 환경일보 기사 추출 """
        html = Crawling.get_text_HwanGyeongnyuseu()
        soup = BeautifulSoup(html, 'html.parser')
        li_tags = soup.find("section", id="section-list"
                    ).find_all("li")

        data = []
        for li in li_tags:
            articles = {}
            em = li.find_all("em")

            articles["title"] = li.h4.text
            articles["reporter"] = em[1].text
            articles["publishing_company"] = "환경신문"
            articles["url"] = f"https://www.hkbs.co.kr/{li.h4.a['href']}"

            # date
            date, time = em[2].text.split()
            date = date.replace(".", "-")
            articles["date"] = f"2022-{date} {time}"
            data.append(articles)

        return data

    @staticmethod
    def get_HanGyeore():
        """ 한겨레 기사 추출 """
        html = Crawling.get_text_HanGyeore()
        soup = BeautifulSoup(html, 'html.parser')
        div_tags = soup.find_all("div", "list")

        data = []
        for div in div_tags:
            articles = {}
            articles["title"] = div.h4.text.strip()
            articles["reporter"] = "-"
            articles["publishing_company"] = "한겨레"
            articles["url"] = f"https://www.hani.co.kr/{div.a['href']}"
            try: # 날짜가 없는 기사, 환경 기사 아닌 속보 기사 제거
                articles["date"] = div.find("span", "date").text
            except AttributeError as e:
                continue
            data.append(articles)

        return data

    @staticmethod
    def get_HwanGyeongbeopryul():
        """ 환경 법률 기사 추출 """
        html = Crawling.get_text_HwanGyeongbeopryul()
        soup = BeautifulSoup(html, 'html.parser')
        td_tags = soup.find_all("td", "ArtList_Title")
        data = []

        for td in td_tags:
            articles = {}
            articles["title"] = td.a.text

            font_tags = td.find_all("font")
            articles["reporter"] = font_tags[1].text.strip()
            articles["publishing_company"] = "환경법률신문"
            articles["url"] = f"http://www.ecolaw.co.kr/news/{td.a['href']}"

            articles["date"] = font_tags[2].text[:-3] # [:-3] 시각 초부분 제거
            data.append(articles)

        return data

    @staticmethod
    def get_HwanGyeongisyu():
        """ 환경 이슈 기사 추출 """
        html = Crawling.get_text_HwanGyeongisyu()
        soup = BeautifulSoup(html, 'html.parser')
        div_tag = soup.find("div", id="sub_read_list")
        div_tags = div_tag.find_all("div", "sub_read_list_box")
        data = []

        for div in div_tags:
            articles = {}
            articles["title"] = div.dt.a.text

            dd_tag = div.find_all("dd")[-1]
            reporter, date = dd_tag.text.split("|")
            articles["reporter"] = reporter.strip()
            articles["publishing_company"] = "환경이슈신문"
            articles["url"] = f"http://www.hkisnews.com/{div.dd.a['href']}"

            articles["date"] = date.strip().replace(".", "-")
            data.append(articles)
        return data

    @staticmethod
    def get_ALL():
        """ 환경 기사 전부 크롤링 """
        article_data = []
        article_data.extend(Articles.get_HwanGyeongnyuseu()) # 환경신문
        article_data.extend(Articles.get_HanGyeore()) # 한겨레
        article_data.extend(Articles.get_HwanGyeongbeopryul()) # 환경 법률
        article_data.extend(Articles.get_HwanGyeongisyu()) # 환경 이슈

        # 시간순으로 정렬
        article_data = sorted(article_data, key=lambda x:x["date"], reverse=True)
        return article_data