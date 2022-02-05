import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth


# key 연동
cred = credentials.Certificate("../DB/json/gdsc-hackathon-cnb-firebase-adminsdk-q06bv-32dcc678c1.json")

firebase_admin.initialize_app(cred)

payload = {
    'display_name': "한태규",
    'email': "gksxorb147@naver.com",
    'phone_number': "01049247067",
    'password': "gksxorb147"
}

# user = auth.create_user(display_name="한태규", email="gksxorb147@naver.com", phone_number="+821012345678", password="gksxorb147")
# user = auth.create_user(payload)

result = auth.get_users([auth.UidIdentifier("JzG9yBlrO2cSSCzlE9Vazx2OJ772")])

for user in result.users:
    print(f"생성완료  : {user.uid}")
    print(f"생성완료  : {user.display_name}")