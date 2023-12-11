import cx_Oracle


def connect_to_database():
    try:
        connected = cx_Oracle.connect('C##Dhanush/dhanush@XE')
        return connected
    except cx_Oracle.Error as e:
        print(e)


def drop_table(connected):
    cursor = connected.cursor()
    try:
        cursor.execute('DROP TABLE Login CASCADE CONSTRAINT')
        cursor.execute('DROP TABLE Train CASCADE CONSTRAINT')
        cursor.execute('DROP TABLE Station  CASCADE CONSTRAINT')
        cursor.execute('DROP TABLE TrainStation CASCADE CONSTRAINT')
        cursor.execute('DROP TABLE Passenger CASCADE CONSTRAINT')
        cursor.execute('DROP TABLE Reservation CASCADE CONSTRAINT')
    except cx_Oracle.Error as e:
        print(e)


# DATABASE
def create_table(connected):
    cursor = connected.cursor()
    try:
        # ENTITY : USER INFORMATION
        cursor.execute("""
                CREATE TABLE Login 
            (   User_name VARCHAR(25),
                Password VARCHAR(20),
                User_Type VARCHAR(25),
                PRIMARY KEY(Password)
            )
             """)

        # ENTITY : TRAIN INFORMATION
        cursor.execute("""
                CREATE TABLE Train
            (   Train_id VARCHAR(9),
                Train_name VARCHAR(25),
                Available_seat NUMBER,
                PRIMARY KEY (Train_id)
            )
             """)

        # ENTITY : STATION DETAILS
        cursor.execute("""
                CREATE TABLE Station
            (
                Station_ID VARCHAR(10),
                Station_name VARCHAR(50),
                PRIMARY KEY(Station_ID)
            )
                """
                       )

        # TrainStations Table (Associative Entity for Many-to-Many Relationship)
        cursor.execute("""
             CREATE TABLE TrainStation
            (
              TrainStationID VARCHAR(25),
              TrainID VARCHAR(25),
              StationID VARCHAR(35),
              DepartureTime varchar(10),
              ArrivalTime varchar(10),
              PRIMARY KEY (TrainStationID),
              FOREIGN KEY (TrainID) REFERENCES Train(Train_id),
              FOREIGN KEY (StationID) REFERENCES Station(Station_ID)
            )
            """)

        # ENTITY : PASSENGER DETAILS
        cursor.execute("""
              CREATE TABLE Passenger
            (
              PassengerID VARCHAR(25) PRIMARY KEY,
              FirstName VARCHAR(50) NOT NULL,
              LastName VARCHAR(50) NOT NULL,
              Email VARCHAR(100)
            )
            """)

        # ENTITY : RESERVATION DETAILS
        cursor.execute("""
              CREATE TABLE Reservation 
            (
              ReservationID INT,
              TrainStationID VARCHAR(25),
              PassengerID VARCHAR(35),
              ReservationDate DATE,
              PRIMARY KEY (ReservationID),
              FOREIGN KEY (TrainStationID) REFERENCES TrainStation(TrainStationID),
              FOREIGN KEY (PassengerID) REFERENCES Passenger(PassengerID)
            )
            """)
        connected.commit()
        cursor.close()
        connected.close()
    except cx_Oracle.Error as e:
        print(e)


# connectedd = connect_to_database()
# drop_table(connectedd)
# create_table(connectedd)


