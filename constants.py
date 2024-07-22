from enum import Enum
import sqlite3
db = sqlite3.connect('server.db')
sql = db.cursor()


class VehicleType(Enum):
    CAR, TRUCK, ELECTRIC, VAN, MOTORBIKE = 1, 2, 3, 4, 5


class ParkingSpotType(Enum):
    CAR, VAN, MOTORBIKE, ELECTRIC = 1, 2, 3, 4


class AccountStatus(Enum):
    ACTIVE, BLOCKED, BANNED, COMPROMISED, ARCHIVED, UNKNOWN = 1, 2, 3, 4, 5, 6


class ParkingTicketStatus(Enum):
    ACTIVE, PAID, LOST = 1, 2, 3


class Address:
    def __init__(self, street, city, state, zip_code, country):
        self.__street_address = street
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__country = country

    def add_address(self, street, city, state, country, zip_code, login):
        sql.execute(f"SELECT login FROM adresses WHERE login=('{login}')")
        if sql.fetchone() is None:
            sql.execute(f"INSERT INTO adresses VALUES (?,?,?,?,?)", (street, city, country, zip_code,state, login))
            db.commit()
            print('Address is added')
        else:
            print("Address already exist")


class Person():
    def __init__(self, name, email, phone):
        self.__name = name
        self.__email = email
        self.__phone = phone

    def add_pers(self, name, password, email, phone):
        sql.execute(f"SELECT login FROM accounts WHERE login='{name}'")
        if sql.fetchone() is None:
            sql.execute(f"INSERT INTO accounts VALUES (?,?,?,?,?)", (name, password, email, phone, 'USER'))
            db.commit()
            print('CREATED in')
        else:
            print("LOgin already exist")
