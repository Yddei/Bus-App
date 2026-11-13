from services.travel_time import get_bus_travel_time


def main():
    start_stop_id = input("Enter bus stop ID: ")
    dest_stop_id = input("Enter destination ID: ")
    bus_number = input("Enter bus number: ")

    result = get_bus_travel_time(start_stop_id, dest_stop_id, bus_number)
    if result is None:
        print("No matching bus with a valid travel time was found at both stops.")
        return

    print(f"Bus {result['service_no']} travel time: {result['travel_time_seconds'] / 60:.1f} minutes")
    print(f"Arrival at start: {result['start_arrival']}")
    print(f"Arrival at destination: {result['destination_arrival']}")

if __name__ == "__main__":
    main()
