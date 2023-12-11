# TO CREATE THE LOGIN OBJECT
import cx_Oracle

from table import connect_to_database


class Login:
    def __init__(self, name: str, password: str, Type='user'):
        self.name = name
        self.password = password
        self._type = Type

    def value(self):
        return self.name, self.password, self._type

    def register_user(self):
        # TO REGISTER THE USER
        connected = connect_to_database()
        cursor = connected.cursor()
        try:
            query = "INSERT INTO Login(USER_NAME, PASSWORD, USER_TYPE) VALUES(:name, :password, :Type)"
            params = {'name': self.name, 'password': self.password, 'Type': self._type}

            cursor.execute(
                    query, params
                )
            connected.commit()
            cursor.close()
            connected.close()
        except cx_Oracle.Error as e:
            print(e)


if __name__ == "__main__":
    p1 = Login("gavutham", "asdf12345",)
    p1.register_user()
