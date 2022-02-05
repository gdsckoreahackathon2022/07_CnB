import json
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


class Singleton(object):
    """ 싱글턴 적용 """
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance


class FirestoreConnect(Singleton):
    """ Firestore 접속 """

    FILE_PATH: str = os.path.dirname(__file__)
    URL_FILE_PATH: str = F"{FILE_PATH}/json/DB_URL.json"
    CREDENTIALS_FILE_PATH: str = f"{FILE_PATH}/json/gdsc-hackathon-cnb-firebase-adminsdk-q06bv-32dcc678c1.json"

    # json file load
    with open(URL_FILE_PATH, "r") as json_file:
        url_json = json.load(json_file)

    # 접속
    _cred: object = credentials.Certificate(CREDENTIALS_FILE_PATH)
    _default_app: object = firebase_admin.initialize_app(_cred, {
        'databaseURL': URL_FILE_PATH
    })
    _db: object = firestore.client()

    def set(cls, collection: str, document: str, **data):
        """ 데이터 수정 및 생성 """
        dec_ref = cls._db.collection(collection).document(document)
        dec_ref.set(data)

    def get(cls, collection: str) -> dict:
        """ 데이터 얻기 """
        docs = cls._db.collection(collection).stream()
        val = {}
        for doc in docs:
            val[doc.id] = doc.to_dict()
        return val

    def set_quiz(cls, collection, document, **data):
        """ quiz 데이터 수정 및 생성 """
        cls.set(collection, document, **data)

    def get_quiz(cls, collection="quiz") -> dict:
        """ quiz 퀴즈 얻기 """
        return cls.get(collection)

    def set_news(cls, collection, document, **data):
        """ news 데이터 수정 및 생성 """
        cls.set(collection, document, **data)

    def get_news(cls, collection="news") -> dict:
        """ news 데이터 얻기 """
        return cls.get(collection)

    def set_mission(cls, collection, document, **data):
        """ mission 데이터 수정 및 생성 """
        cls.set(collection, document, **data)

    def get_mission(cls, collection="mission") -> dict:
        """ mission 데이터 얻기 """
        return cls.get(collection)

    def set_user(cls, collection, document, **data):
        """ user 데이터 수정 및 생성 """
        cls.set(collection, document, **data)

    def get_user(cls, collection="user") -> dict:
        """ user 데이터 얻기 """
        return cls.get(collection)

    def set_rank(cls, collection, document, **data):
        """ rank 데이터 수정 및 생성 """
        cls.set(collection, document, **data)

    def get_rank(cls, collection="user") -> dict:
        """ rank 데이터 얻기 """
        return cls.get(collection)

    def set_temperature(cls, collection, document, **data):
        """ temperature 데이터 수정 및 생성 """
        cls.set(collection, document, **data)

    def get_temperature(cls, collection="user") -> dict:
        """ temperature 데이터 얻기 """
        return cls.get(collection)