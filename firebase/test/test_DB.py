import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# key 연동
cred = credentials.Certificate("./DB/json/gdsc-hackathon-cnb-firebase-adminsdk-q06bv-32dcc678c1.json")

# DB URL
db_url = 'https://gdsc-hackathon-cnb.firebaseio.com/'

default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': db_url
})

db = firestore.client()
dec_ref = db.collection("quiz").document("1")
dec_ref.set({
    "answer":{
        "0": True,
        "0": False
    },
    "question": "세번째 질문입니다."
}, merge=True)