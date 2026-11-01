#from services.bus_routes import get_buses_by_stop
from services.bus_arrivals import get_bus_arrivals


stop_id = input("Enter bus stop ID: ")
bus_number = input("Enter bus number: ")

print(get_bus_arrivals(stop_id, bus_number))