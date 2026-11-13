#from services.bus_routes import get_buses_by_stop
from services.bus_arrivals import get_bus_arrivals


start_stop_id = input("Enter bus stop ID: ")
dest_stop_id = input("Enter destination ID")
bus_number = input("Enter bus number: ")

start_stop = get_bus_arrivals(start_stop_id, bus_number)
dest_stop = get_bus_arrivals(dest_stop_id, bus_number)

main_bus = start_stop.NextBus()
main_bus_location = [main_bus.Latitude(), main_bus.Longitude()]

#if main_bus_location == [dest_stop.NextBus().Latitude(), dest_stop.NextBus().Longitude()]:
