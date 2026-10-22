#this is for initial fetch of api
#im testing waters


import os
import requests
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("LTA_API_KEY")

if not API_KEY:
    raise RuntimeError("go get an API key and put into .env")


#may put inside a try/except later, and maybe that will go inside a function too
get_busstop = requests.get(
    "https://datamall2.mytransport.sg/ltaodataservice/BusStops",
    headers={
        "AccountKey": API_KEY,
        "accept": "application/json"
    },
    timeout=15
)

get_busstop.raise_for_status()
data = get_busstop.json()





for bus_stop in data["value"][:3]:
    print(bus_stop)