from crawling.crawling import Articles
from DB.firebase_connect import FirestoreConnect

class FirestoreNews:

    @staticmethod
    def set_data():
        """ 데이터 넣기 """
        FC = FirestoreConnect()
        article_data = Articles.get_ALL()
        for index, data in enumerate(article_data[:10]): # < 뉴스기사 10개만
            print(data)
            FC.set_news(collection="news", document=f"{index}", **data)
        return