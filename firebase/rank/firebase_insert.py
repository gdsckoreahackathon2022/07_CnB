from DB.firebase_connect import FirestoreConnect

class FirestoreRank:

    @staticmethod
    def set_rank():
        """ 랭크 데이터 초기화 """
        FC = FirestoreConnect()
        users_data = FC.get(collection="user")
        rank_data = {}

        for uid, data in users_data.items():
            rank_data[uid] = {
                "name": data["name"],
                "point_sum": data["point_sum"]
            }

        # 데이터 삽입
        FC.set_rank(collection="rank", document="rank", **rank_data)