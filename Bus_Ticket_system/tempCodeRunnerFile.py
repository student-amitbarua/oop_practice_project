from abc import ABC, abstractclassmethod

class AbstractBus(ABC):
    def __init__(self, coach, driver, arrival, departure, from_des, to) ->None:
        self.coach = coach
        self.driver = driver
        self.arrival = arrival
        self.departure = departure
        self.from_des = from_des
        self.to = to
        self.seats = ['empty' for _ in range(20)]


class Bus(AbstractBus):
    pass
        
class BusCompany:
    def __init__(self) -> None:
        self.buses = {}

    def install_bus(self, bus):
        self.buses[bus.coach] = bus


    def display_available_buses(self):

        if not self.buses:
            print("NO buses are available")

        else: 
            print(f'coach\tDriver\tArrival\tDeparture\tFrom\tTo')
            for coach, bus in self.buses.items():
                print(f'{coach}\t{bus.driver}\t{bus.arrival}\t{bus.departure}\t{bus.from_des}\t{bus.to}')

                def book_ticket(self, coach, seat):
                    if coach in self.buses:
                        if 1>=seat<=20:
                            if self.buses[coach].seats[seat - 1] == 'Empty':
                                self.buses[coach].seats[seat - 1] = 'Booked'

                            else:
                                print('seat already booked!!')

                        else: 
                            print('Invalid seat number')

                    else:
                        print('Invalid coach number')

                def display_seat_status(self, coach):
                    if coach in self.buses:
                        print(self.buses[coach].seats)

                
bus1 = Bus(2, 'Rahim', '9pm', '9:30pm', 'Dhaka', 'Sylhet')

company = BusCompany()
company.install_bus(bus1)
print(company.display_available_buses())
print(company.display_seat_status(2))