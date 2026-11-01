import os

import requests
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("LTA_API_KEY")


def get_bus_arrivals(bus_stop_id, bus_number):
    if not API_KEY:
        raise RuntimeError("Set LTA_API_KEY in .env before fetching bus arrivals")

    bus_stop_id = str(bus_stop_id).strip()
    bus_number = str(bus_number).strip()
    if not bus_stop_id or not bus_number:
        raise ValueError("Bus stop ID and bus number are both required")

    response = requests.get(
        "https://datamall2.mytransport.sg/ltaodataservice/v3/BusArrival",
        headers={
            "AccountKey": API_KEY,
            "accept": "application/json",
        },
        params={"BusStopCode": bus_stop_id, "ServiceNo": bus_number},
        timeout=30,
    )
    response.raise_for_status()
    return response.json()