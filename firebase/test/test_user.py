import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


# key 연동
cred = credentials.Certificate("../DB/json/gdsc-hackathon-cnb-firebase-adminsdk-q06bv-32dcc678c1.json")

firebase_admin.initialize_app(cred)

db = firestore.client()
docs = db.collection('user').stream()

for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')