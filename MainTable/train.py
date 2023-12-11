from table import connect_to_database
import cx_Oracle


class Train:
    def __init__(self, name, train_id, available_seat):
        self.train_name = name
        self.train_id = train_id
        self.available_seat = available_seat

    def values(self):
        return self.train_id, self.train_name, self.available_seat

    def insert_train(self):
        """

        :rtype: object
        """
        connected = connect_to_database()
        cursor = connected.cursor()
        try:
            query = "INSERT INTO Train(TRAIN_NAME, TRAIN_ID, AVAILABLE_SEAT) VALUES(:train_id, :train_name, :seat)"
            params = {'train_id': self.train_id, 'train_name': self.train_name, 'seat': self.available_seat}

            cursor.execute(
                    query, params
                )
            connected.commit()
            cursor.close()
            connected.close()
        except cx_Oracle.Error as e:
            print(e)


if __name__ == "__main__":
    t1 = Train("avadi5122", "avadi expRESS", 2034)
    t1.insert_train()
