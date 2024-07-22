import sqlite3
from constants import Person, Address
from account import Admin, ParkingAttendant
from PaymentMethod import PaymentMethod
from ParkingLot import ParkingLot

db = sqlite3.connect('server.db')
sql = db.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS accounts(
login TEXT,
password TEXT,
email TEXT,
phone TEXT,
acc_type TEXT
)""")
sql.execute("""CREATE TABLE IF NOT EXISTS adresses(
street TEXT,
city TEXT,
country TEXT,
zip_code TEXT,
state TEXT
user_name TEXT
)""")
db.commit()
db.close()
print("input parking name num of floors and slot per floor: ")
create_parking = list(input().split())
parkingLot = ParkingLot(create_parking[0], int(create_parking[1]), int(create_parking[2]))

choice = input('Login (1.Admin; 2.parking attendant, 3.Register new parking attendant,4. exit): ')
while True:
    if choice == "1":
        admin_login = input('Admin Login: ')
        admin_password = input('Admin pass: ')
        admin_log = Admin(admin_login, admin_password, )
        if admin_log.admin_logIn(admin_login, admin_password):

            admin_choice = input('(1.display free slots; 2.display occupied slots, 3.add floor,4.add spot , 5. exit): ')
            if admin_choice == "1":
                display_input = list(input("Input the type of vehicle: ").split())
                parkingLot.display_free_spots(display_input[0])
            elif admin_choice == "2":
                display_input = list(input("Input the type of vehicle: ").split())
                parkingLot.display_occupied_spots(display_input[0])
            elif admin_choice == "3":
                display_input = list(input("Input num of spots of the new floor: ").split())
                parkingLot.add_floor(int(display_input[0]))
            elif admin_choice == "4":
                display_input = list(input("Input the num of floor and vehicle type:  ").split())
                parkingLot.add_parking_spot_to_floor(int(display_input[0]), display_input[1])
            elif admin_choice== "5":
                print("program exit")
                break
            else: print('Please choose between 1-4')

        else:
            choice = input('Login (1.Admin; 2.parking attendant, 3.Register new parking attendant,4. exit): ')

    elif choice == "2":
        user_login = input('Login: ')
        user_password = input('pass: ')
        user = ParkingAttendant(user_login, user_password)
        if user.attendant_login(user_login, user_password):
            user_choice = input('(1.display free slots; 2.display occupied slots, 3.park car, 4.remove car 5. exit): ')
            if user_choice == "1":
                display_input = list(input("Input the type of vehicle: ").split())
                parkingLot.display_free_spots(display_input[0])

            elif user_choice == "2":
                display_input = list(input("Input the type of vehicle: ").split())
                parkingLot.display_occupied_spots(display_input[0])
            elif user_choice == "3":
                display_input = list(input("Input the details of vehicle: ").split())
                check = parkingLot.register_car(display_input[0], display_input[1])
                if check != None:
                    print(
                        f"Parked vehicle. Ticket ID: {check}"
                    )
            elif user_choice == "4":
                display_input = list(input("Input the ticket ID: ").split())
                parkingLot.unpark(parkingLot.tickets[display_input[1]].floor, parkingLot.tickets[display_input[1]].spot)
                parkingLot.payment(parkingLot.tickets[display_input[1]])
                payment_method= PaymentMethod()
                payment_method.select_payment_method()
                parkingLot.payment(parkingLot.tickets[display_input[1]])
            elif user_choice=="5":
                print("program exit")
                break
            else:
                print('Please choose between 1-4')





        else:
            choice = input('Login (1.Admin; 2.parking attendant, 3.Register new parking attendant,4. exit): ')

    elif choice == "4":
        print("program exit")
        break
    elif choice == "3":
        new_login = input('Login: ')
        new_password = input('Pass: ')
        user_phone = input('Phone: ')
        user_email = input('Email: ')
        new_user = Person(new_login, user_email, user_phone)
        new_user.add_pers(new_login, new_password, user_email, user_phone)
        user_str = input('street: ')
        user_city = input('city: ')
        user_country = input('country: ')
        user_state = input('state: ')
        user_zipcode = input('zip code: ')
        address = Address(user_str, user_city, user_state, user_zipcode, user_country)
        address.add_address(user_str, user_city, user_state, user_zipcode, user_country, new_login)
        choice = input('Login (1.Admin; 2.parking attendant, 3.Register new parking attendant,4. exit): ')
    else:
        print('Please choose between 1-4')
        choice = input('Login (1.Admin; 2.parking attendant, 3.Register new parking attendant,4. exit): ')
