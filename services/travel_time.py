from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from decimal import Decimal, InvalidOperation

from services.bus_arrivals import get_bus_arrivals

# compares location of bus at time of query to identify the same bus
def _bus_identity(bus):
    try:
        latitude = Decimal(str(bus.get("Latitude", "")))
        longitude = Decimal(str(bus.get("Longitude", "")))
    except InvalidOperation:
        return None
    if not latitude.is_finite() or not longitude.is_finite():
        return None
    if latitude == 0 or longitude == 0:
        return None
    origin = bus.get("OriginCode")
    destination = bus.get("DestinationCode")
    if not origin or not destination:
        return None
    return latitude, longitude, origin, destination


def _arrival_time(bus):
    try:
        arrival = datetime.fromisoformat(bus.get("EstimatedArrival", ""))
    except (TypeError, ValueError):
        return None
    return arrival if arrival.utcoffset() is not None else None

# looks like time complexity is O(n^2) but n is small (3 buses per stop) so it should be fine
def calculate_travel_time(start_data, destination_data, bus_number):
    bus_number = str(bus_number).strip()
    matches = []
    for start_service in start_data.get("Services", []):
        if str(start_service.get("ServiceNo")) != bus_number:
            continue
        for destination_service in destination_data.get("Services", []):
            if str(destination_service.get("ServiceNo")) != bus_number:
                continue
            for start_key in ("NextBus", "NextBus2", "NextBus3"):
                start_bus = start_service.get(start_key) or {}
                identity = _bus_identity(start_bus)
                start_time = _arrival_time(start_bus)
                if identity is None or start_time is None:
                    continue
                for destination_key in ("NextBus", "NextBus2", "NextBus3"):
                    destination_bus = destination_service.get(destination_key) or {}
                    if _bus_identity(destination_bus) != identity:
                        continue
                    destination_time = _arrival_time(destination_bus)
                    if destination_time is None or destination_time <= start_time:
                        continue
                    matches.append((start_time, {
                        "service_no": bus_number,
                        "start_arrival": start_time.isoformat(),
                        "destination_arrival": destination_time.isoformat(),
                        "travel_time_seconds": (destination_time - start_time).total_seconds(),
                    }))
    return min(matches, key=lambda match: match[0])[1] if matches else None


def get_bus_travel_time(start_stop_id, destination_stop_id, bus_number):
    if str(start_stop_id).strip() == str(destination_stop_id).strip():
        raise ValueError("Start and destination stops must be different")
    with ThreadPoolExecutor(max_workers=2) as executor:
        start = executor.submit(get_bus_arrivals, start_stop_id, bus_number)
        destination = executor.submit(get_bus_arrivals, destination_stop_id, bus_number)
        return calculate_travel_time(start.result(), destination.result(), bus_number)
