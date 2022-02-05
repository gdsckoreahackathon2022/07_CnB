import json
import os
from DB.firebase_connect import FirestoreConnect

class FirestoreMission:

    FILE_PATH: str = os.path.dirname(__file__)
    MISSION_FILE_PATH: str = F"{FILE_PATH}/json/mission.json"

    @staticmethod
    def set_data():
        """ 데이터 넣기 """
        FC = FirestoreConnect()

        # json file read
        with open(FirestoreMission.MISSION_FILE_PATH,
                  encoding='UTF8') as json_file:
            missions = json.load(json_file)

        for index, mission in missions.items():
            FC.set_mission(collection="mission", document=f"{index}", **mission)