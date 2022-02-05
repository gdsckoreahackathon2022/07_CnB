import unittest
from crawling.crawling import (
    Http, Crawling, Articles
)

class TestBlockToMarkdown(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """테스트를 실행할 때 단 1번 실행 됩니다."""
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        """테스트를 끝낼 때 단 1번 실행 됩니다."""
        print('teardownClass')

    def setUp(self):
        """각각의 테스트 메소드가 실행될 때 실행 됩니다."""
        print('setUp')

    def tearDown(self):
        """각각의 테스트 메소드가 끝날 때 실행 됩니다."""
        print('tearDown\n')

    def test_get_text(self):
        """ text 오는지 확인 """
        url = "https://beomi.github.io/gb-crawling/posts/2017-01-20-HowToMakeWebCrawler.html"
        print(Http.get_text(url))

    def test_get_text_HwanGyeongnyuseu(self):
        """ 환경일보 html get 테스트 """
        print(Crawling.get_text_HwanGyeongnyuseu())

    def test_get_text_HanGyeore(self):
        """ 한겨레 html get 테스트 """
        print(Crawling.get_text_HanGyeore())

    def test_get_text_HwanGyeongbeopryul(self):
        """ 환경 이슈 html get 테스트 """
        print(Crawling.get_text_HwanGyeongbeopryul())

    def test_get_text_HwanGyeongisyu(self):
        """ 환경 이슈 html get 테스트 """
        print(Crawling.get_text_HwanGyeongisyu())

    def _show_data(self, data: list) -> None:
        for row in data:
            print(row)

    def test_articles_get_HwanGyeongnyuseu(self):
        """ 환경일보 기사 크롤링 테스트 """
        data = Articles.get_HwanGyeongnyuseu()
        self._show_data(data)

    def test_articles_get_HanGyeore(self):
        """ 한겨레 기사 크롤링 테스트 """
        data = Articles.get_HanGyeore()
        self._show_data(data)

    def test_articles_get_HwanGyeongbeopryul(self):
        """ 환경 법률 기사 크롤링 테스트 """
        data = Articles.get_HwanGyeongbeopryul()
        self._show_data(data)

    def test_articles_get_HwanGyeongisyu(self):
        """ 환경 이슈 기사 크롤링 테스트 """
        data = Articles.get_HwanGyeongisyu()
        self._show_data(data)

    def test_articles_get_ALL(self):
        """ 환경 기사 전부 크롤링 테스트 """
        self._show_data(Articles.get_ALL())