from ride import Ride, RideRequest, RideMatching, RideSharing
from users import Rider, Driver
from vehicle import Car, Bike

niye_jao = RideSharing("Niye Jao")

rahim = Rider('Rahim uddin', 'rahim@gmail.com', 1234, 'Mohakhali', 1200 )

niye_jao.add_rider(rahim)
print(niye_jao)

kolimuddin = Driver('kolim uddim ', 'kolim@gmail.com', 1256, 'Gulshan')
niye_jao.add_driver(kolimuddin)

rahim.request_ride(niye_jao, 'uttara', 'car')


kolimuddin.reach_destination(rahim.current_ride)
rahim.show_current_ride()
