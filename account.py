from constants import *
import sqlite3
db = sqlite3.connect('server.db')
sql = db.cursor()

class Account:
    def __init__(self, user_name, password):
        self.__user_name = user_name
        self.__password = password



    def reset_password(self, new_pass):
        self.__password = new_pass

    #def login(self, user_name, password):
     #   self.__user_name = user_name
      #  self.__password = password
       # sql.execute(f"SELECT login,password FROM accounts WHERE login=('{user_name}') AND password=('{password}')")
        #if sql.fetchone() is not None:
         #   print('you logged')


class Admin(Account):
    def __init__(self, user_name, password):
        super().__init__(user_name, password)

    def admin_logIn(self, login, password):
        if login=="exit":
            print("program exit")
            exit()

        sql.execute(f"SELECT login,password FROM accounts WHERE login='{login}' AND password='{password}' AND acc_type='ADMIN'")
        if sql.fetchone() is not None:
            db.commit()
            print('you logged')
            return True
        else:
            print('wrong pass')
            return False




class ParkingAttendant(Account):
    def __init__(self, user_name, password):
        super().__init__(user_name, password)
        self.carNumber = None
        self.status = None

    def car_number(self, status, carNumber):
        self.status = status
        self.carNumber = carNumber
    def attendant_login(self,login,password):
        if login=="exit":
            print("program exit")
            exit()
        sql.execute(
            f"SELECT login,password FROM accounts WHERE login='{login}' AND password='{password}' AND acc_type='USER'")
        if sql.fetchone() is not None:
            db.commit()
            print('you logged')
            return True
        else:
            print('wrong pass')
            return False

    def process_ticket(self, ticket_number):
        print('')
