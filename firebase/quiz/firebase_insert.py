import json
import os
from DB.firebase_connect import FirestoreConnect

class FirestoreQuiz:

    FILE_PATH: str = os.path.dirname(__file__)
    QUIZ_FILE_PATH: str = F"{FILE_PATH}/json/quiz.json"

    @staticmethod
    def set_data():
        """ 데이터 넣기 """
        FC = FirestoreConnect()

        # json file read
        with open(FirestoreQuiz.QUIZ_FILE_PATH,
                  encoding='UTF8') as json_file:
            quizs = json.load(json_file)

        for index, quiz in quizs.items():
            FC.set_mission(collection="quiz", document=f"{index}", **quiz)