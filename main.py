from services.bus_routes import get_buses_by_stop

get_id_user = int(input("Enter Bus ID: "))

result = get_buses_by_stop(get_id_user)

print(result)