# Python Part
Flutter 엡에서 사용하는 데이터를 Firebase에 넣어주는 code입니다.

데이터의 종류
- News 크롤링 기사 데이터
- Quiz 데이터
- Mission 데이터
- 기온 데이터
- User 테스트 데이터

## Version
- python : `3.10.1`
- firebase-admin : `5.2.0`
- beautifulsoup4 : `4.10.0`
- requests : `2.27.1`

## 폴더 구조
```text
│
├─crawling # 크롤링 
│      crawling.py # 환경 뉴스 크롤링
│      firebase_insert.py # 뉴스 데이터 Firebase에 넣기
├─DB
│  │  firebase_connect.py # Firebase 연결
│  └─json
│     # Firebase 연결 key
│     # 비공개
│ 
├─mission # 미션
│  │  firebase_insert.py # 미션 데이터 Firebase에 넣기
│  └─json # 미션 데이터
│          mission.json
│ 
├─quiz # 퀴즈
│  │  firebase_insert.py # 미션 데이터 Firebase에 넣기
│  └─json # 퀴즈 데이터
│          quiz.json
│ 
├─rank # 순위
│      firebase_insert.py # 사용자 순위 데이터 Firebase에 넣기
│ 
├─temperature # 기온
│  │  firebase_insert.py # 기온 데이터 Firebase에 넣기
│  │ 
│  └─csv # 기온 데이터
│          temper_2000.csv
│          temper_2012.csv
│          temper_2017.csv
│          temper_2022.csv
│
└─test # 테스트 코드
    │  test_auth.py  # User 정보 확인
    │  test_DB.py # Firebase 연동 확인
    │  test_user.py # 모든 User 확인
    ├─crawling # 크롤링 test
    │      test_crawling.py
    │      test_firebase_insert.py
    ├─DB # 데이터 삽입 test
    │      test_firebase_connect.py
    ├─mission # 미션 test
    │      test_firebase_insert.py
    ├─quiz # 퀴즈 test  
    │      test_firebase_insert.py
    ├─rank # 순위 test  
    │      test_firebase_insert.py
    └─temperature # 기온 test  
            test_firebase_insert.py
```
