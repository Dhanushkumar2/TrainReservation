from table import connect_to_database
import cx_Oracle

class Station:
    def __init__(self, name, station_id):
        self.station_name = name
        self.station_id = station_id

    def value(self):
        return self.station_id, self.station_name

    def insert(self):
        connected = connect_to_database()
        cursor = connected.cursor()
        try:
            query = "INSERT INTO Station(STATION_ID, STATION_NAME) VALUES(:station_id, :station_name)"
            params = {'station_name': self.station_name, 'station_id': self.station_id}

            cursor.execute(
                    query, params
                )
            connected.commit()
            cursor.close()
            connected.close()
        except cx_Oracle.Error as e:
            print(e)


if __name__ == "__main__":
    s1 = Station("erode", "001stat")
    s1.insert()
