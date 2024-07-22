from datetime import datetime
from uuid import uuid4
from constants import *
from ParkingSpot import CarSpot, MotorbikeSpot, ElectricSpot, VanSpot
import time

current_datetime = datetime.now().strftime('%Y%m-%d%H-%M%S-') + str(uuid4())


class ParkingFloor:
    def __init__(self, floor, spots):
        self.spots = []
        self.__spots = []
        self.floor = floor
        self.__numberOfSpots = 0
        car_spots = spots // 4
        van_spots = spots // 4
        motorbike_spots = spots // 4
        electric_spots = spots // 4

        # Create spots for each vehicle type
        for _ in range(car_spots):
            self.spots.append(CarSpot(len(self.spots)))
        for _ in range(van_spots):
            self.spots.append(VanSpot(len(self.spots)))
        for _ in range(motorbike_spots):
            self.spots.append(MotorbikeSpot(len(self.spots)))
        for _ in range(electric_spots):
            self.spots.append(ElectricSpot(len(self.spots)))
        remaining_spots = spots - (car_spots + van_spots + motorbike_spots + electric_spots)
        for _ in range(remaining_spots):
            self.spots.append(CarSpot(len(self.spots) + 1))

        self.__numberOfSpots = spots
        self.__numberOfSpots = spots

    def isFullFloor(self, type) -> bool:
        for spot in self.spots:
            if spot.type.name == type and spot.free == True:
                return True
        return False

    def showFreeSpot(self, type):
        return [spot.spot_number + 1 for spot in self.spots if spot.free and spot.type.name == type]

    def showOccupiedSpot(self, type):
        return [spot.spot_number + 1 for spot in self.spots if not spot.free and spot.type.name == type]


class ParkingTicket:
    def __init__(
            self, ticketID, ticketStatus, payedAmount, carNumber, floor, spot, vehicleType
    ):
        self.ticketId = ticketID
        self.arriveTime = datetime.now()
        self.ticketStatus = ticketStatus
        self.payedAmount = payedAmount
        self.leaveTime = None
        self.carNumber = carNumber
        self.floor = floor
        self.spot = spot
        self.vehicleType = vehicleType

    def getId(self):
        ticket = self.ticketId
        return ticket


class ParkingLot:

    def __init__(self, parking_id, num_of_floors, num_of_slots):
        self.id = parking_id
        self.num_of_floors = num_of_floors
        self.__floors = []
        self.tickets = {}
        for i in range(num_of_floors):
            self.__floors.append(ParkingFloor(i, num_of_slots))
        print('created parkingLOT with', num_of_slots)

    def register_car(self, carNumber, carType):
        current_datetime = datetime.now().strftime('%Y%m%d ') + carNumber + " "
        parking_floor, parking_spot = self.park(carType)

        if parking_floor is not None and parking_spot is not None:
            ticket_id = self.generate_ticket_id(carNumber, parking_floor, parking_spot)
            self.create_ticket(ticket_id, carNumber, parking_floor, parking_spot, carType)
            return ticket_id
        else:
            print("No available spot for the vehicle.")
            return None

    def generate_ticket_id(self, carNumber, floor, spot):
        ticket_id = datetime.now().strftime('%Y%m%d%H%M%S ') + carNumber + ' ' + str(floor) + ' ' + str(spot)
        return ticket_id

    def create_ticket(self, ticket_id, carNumber, floor, spot, carType):
        ticket = ParkingTicket(
            ticket_id,
            ParkingTicketStatus.ACTIVE,
            0,
            carNumber,
            floor,
            spot,
            carType
        )
        self.tickets[carNumber] = ticket

    def display_count(self, type):
        for floor in self.__floors:
            freeSpots = floor.showFreeSpot(type)
            print(
                f"Number of free spots for {type} on Floor {floor.floor}: {len(freeSpots)}"
            )

    def display_free_spots(self, type):
        for floor_number, floor in enumerate(self.__floors, start=1):
            free_spots = floor.showFreeSpot(type)
            if not free_spots:
                print(f"No free spots for {type} in Floor {floor_number}")
            else:
                print(f"Free spots for {type} on Floor {floor_number}: {free_spots}")

    def payment(self, ticket: ParkingTicket):
        if ticket.ticketStatus == ParkingTicketStatus.PAID:
            print(f"Vehicle {ticket.carNumber} already paid {ticket.payedAmount}")
        elif ticket.ticketStatus == ParkingTicketStatus.ACTIVE:
            current_time = datetime.now()
            parked_duration = current_time - ticket.arriveTime
            parked_hours = parked_duration.total_seconds() // 3600
            payment_amount = self.calculate_payment_amount(parked_hours)
            print(f"Vehicle {ticket.carNumber} parked for {parked_hours} hours. You should pay ${payment_amount:.2f}")
            ticket.payedAmount = payment_amount
            ticket.ticketStatus = ParkingTicketStatus.PAID

    def calculate_payment_amount(self, parked_hours):
        # Per-hour parking fee model
        # parked_hours += 1
        first_hour_rate = 4
        second_third_hour_rate = 3.5
        remaining_hour_rate = 2.5

        if parked_hours == 0:
            return 0
        elif parked_hours == 1:
            return first_hour_rate
        elif parked_hours <= 3:
            return first_hour_rate + (parked_hours - 1) * second_third_hour_rate
        else:
            return first_hour_rate + 2 * second_third_hour_rate + (parked_hours - 3) * remaining_hour_rate

    def display_occupied_spots(self, type):
        for floor_number, floor in enumerate(self.__floors, start=1):
            occupied_spots = floor.showOccupiedSpot(type)
            if not occupied_spots:
                print(f"No occupied spots for {type} in Floor {floor_number}")
            else:
                print(f"Occupied spots for {type} on Floor {floor_number}: {occupied_spots}")

    def park(self, type):
        for floor_number, floor in enumerate(self.__floors, start=1):
            for spot_number, spot in enumerate(floor.spots, start=1):
                if spot.free and spot.type.name == type:
                    spot.free = False
                    return floor_number, spot_number
        return None

    def unpark(self, floorNumber, spotNumber):
        floorNumber -= 1
        spotNumber -= 1
        self.__floors[floorNumber].spots[spotNumber].free = True
        print('Vehicle in floor', floorNumber, 'and in spot', spotNumber, ' is removed')

    def add_floor(self, num_of_slots):
        new_floor = ParkingFloor(len(self.__floors), num_of_slots)
        self.__floors.append(new_floor)
        print(f"Added new parking floor: {new_floor.floor + 1}")

    def add_parking_spot_to_floor(self, floor_number, spot_type):
        if 0 < floor_number <= len(self.__floors):
            floor = self.__floors[floor_number - 1]
            new_spot_number = len(floor.spots) + 1
            if spot_type == 'CAR':
                new_spot = CarSpot(new_spot_number)
            elif spot_type == 'VAN':
                new_spot = VanSpot(new_spot_number)
            elif spot_type == 'MOTORBIKE':
                new_spot = MotorbikeSpot(new_spot_number)
            elif spot_type == 'ELECTRIC':
                new_spot = ElectricSpot(new_spot_number)
            else:
                print("Invalid spot type.")
                return
            floor.spots.append(new_spot)
            print(f"Added new {spot_type} spot to Floor {floor.floor + 1}: {new_spot_number}")
        else:
            print("Invalid floor number.")
