import os
import csv
from DB.firebase_connect import FirestoreConnect

class FirestoreTemperature:

    FILE_PATH: str = os.path.dirname(__file__)

    TEMPER_2000_PATH: str = F"{FILE_PATH}/csv/temper_2000.csv"
    TEMPER_2022_PATH: str = F"{FILE_PATH}/csv/temper_2022.csv"

    @staticmethod
    def read_temperature_csv(path: str) -> list:
        """ 온도 csv file 읽기 """
        data = []
        with open(path, "r") as csv_file:
            csv_data = csv.reader(csv_file)
            next(csv_file) # header pass
            for time, temperature in csv_data:
                time = str(time).split("-")[1:]
                data.append({
                    "-".join(time):str(temperature)
                })
        return data

    @staticmethod
    def set_temperature():
        """ 온도 데이터 초기화 """
        FC = FirestoreConnect()
        temperature_data = {}

        temperature_data["2000"] = FirestoreTemperature.read_temperature_csv(
                FirestoreTemperature.TEMPER_2000_PATH
            )

        tmp_date = FirestoreTemperature.read_temperature_csv(
                FirestoreTemperature.TEMPER_2022_PATH
            )

        # 예측 나누기
        temperature_data["2022"] = tmp_date[:9]
        temperature_data["prediction"] = tmp_date[9:]

        # 데이터 삽입
        FC.set_temperature(collection="temperature",
                            document="temperature",
                            **temperature_data)