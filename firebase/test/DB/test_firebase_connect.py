import unittest
from DB.firebase_connect import FirestoreConnect

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
        self.F1 = FirestoreConnect()
        self.F2 = FirestoreConnect()

    def tearDown(self):
        """각각의 테스트 메소드가 끝날 때 실행 됩니다."""
        print('tearDown\n')

    def test_singleton(self):
        """ 싱글톤 확인 """
        print(self.F1)
        print(self.F2)

    def test_set_quiz(self):
        """ quiz 데이터 수정 및 생성 테스트 """
        data = {
                "answer":{
                    "0": True,
                    "1": False
                },
                "question": "O,X 질문입니다."
            }
        self.F1.set_quiz(collection="quiz", document="0", **data)

        data = {
                "answer":{
                    "0": False,
                    "1": False,
                    "2": True,
                    "3": False,
                },
                "question": "4지선다 질문입니다."
            }
        self.F1.set_quiz(collection="quiz", document="1", **data)

    def test_get_quize(self):
        """ 모든 quize 얻기 테스트 """
        val = self.F1.get_quiz(collection="quiz")
        print(val)

    def test_set_news(self):
        """ news 데이터 수정 및 생성 테스트 """
        data = {
                "date": "2022-01-29 14:46",
                "URL": "https://www.google.com",
                "title": "뉴스기사 제목",
                "publishing_company": "조선일보",
                "reporter": "기자이름"
            }

        self.F1.set_news(collection="news", document="3", **data)

    def test_get_news(self):
        """ news 뉴스 얻기 테스트 """
        val = self.F1.get(collection="news")
        print(val)

    def test_set_mission(self):
        """ mission 수정 및 생성 테스트 """
        data = {
            "point": 0,
            "title": "쓰레기 5개 줍기",
            "info": "주변의 쓰레기 5개를 주워주세요!",
            "week_check": False
        }
        for i in range(0, 4):
            self.F1.set_mission(collection="mission", document=f"{i}", **data)

    def test_get_mission(self):
        """ mission 얻기 테스트 """
        val = self.F1.get(collection="mission")
        print(val)

    def test_set_user(self):
        """ user 수정 및 생성 테스트 """
        mission_dict = self.F1.get(collection="mission")
        data = {
            "point_sum": 0,
            "name": "현주엽",
            "mission": mission_dict
        }
        self.F1.set_user(collection="user", document="JzG9yBlrO2cSSCzlE9Vazx2OJ772", **data)

