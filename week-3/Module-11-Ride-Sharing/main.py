
from ride import RideShaing , Ride, RideRequest, RideMatching
from user import Rider , User, Driver
from vehical import Car, Bike


niye_jao = RideShaing("Niye jao")
rahim = Rider("Rahim", "rahim@gmail.com", 1234,"Mohakhali", 1200)
niye_jao.add_rider(rahim)
kolimuddin = Driver("Kolim Uddin", "koli@gmail.com", 1256, "Gulshan")
niye_jao.add_driver(kolimuddin)


print(niye_jao)

