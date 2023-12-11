from MainTable.table import connect_to_database
import cx_Oracle
from MainTable.train import *


def admin_login(name, password):
    # VERIFICATION OF  USER
    # global rows
    connected = connect_to_database()
    try:
        cursor = connected.cursor()
        admin = "admin"
        query = "SELECT * FROM LOGIN WHERE User_Type = :admin"
        cursor.execute(query, admin=admin)
        rows = cursor.fetchall()
        for row in rows:
            if row[0] != name and row[1] != password:
                print(row)
                return "INVALID USER NAME OR PASSWORD"
            return "VALID USER"
        cursor.close()
        connected.close()
    except cx_Oracle.Error as e:
        print(e)


def add_train():
    train_name = input("ENTER THE TRAIN NAME: ")
    train_id = input("ENTER THE TRAIN ID: ")
    available = input("ENTER THE AVAILABLE SEAT: ")
    t1 = Train(train_name, train_id, available)
    t1.insert_train()


if __name__ == "__main__":
    print(admin_login("asdf", "asdf"))
