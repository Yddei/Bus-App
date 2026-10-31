#this is for initial fetch of api
#run this to fetch bus routes into local database first


import os
import requests
from dotenv import load_dotenv
import mysql.connector

#env variables
load_dotenv()
API_KEY = os.getenv("LTA_API_KEY")

if not API_KEY:
    raise RuntimeError("go get an API key and put into .env")

#temp sql connector function
def conn_db():
    return mysql.connector.connect(
        host = os.getenv("MYSQL_HOST"),
        port = int(os.getenv("MYSQL_PORT")),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_ROOT_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE")
    )


def get_bus_routes():
    routes = []
    skip = 0

    while True:
        response = requests.get(
            "https://datamall2.mytransport.sg/ltaodataservice/BusRoutes",
            headers={
                "AccountKey": API_KEY,
                "accept": "application/json"
            },
            params={"$skip": skip},
            timeout=30
        )

        response.raise_for_status()

        batch = response.json()["value"]
        routes.extend(batch)

        print(f"Fetched {len(batch)} records, total: {len(routes)}")

        if len(batch) < 500:
            break

        skip += 500

    return routes


#temp, delete later
routes = get_bus_routes()
def insert_bus_routes(routes):
    conn = conn_db()
    cursor = conn.cursor()

    query = """
        INSERT INTO bus_routes (
            service_no,
            direction,
            stop_sequence,
            bus_stop_code,
            distance
        )

        VALUES (%s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            bus_stop_code = VALUES(bus_stop_code),
            distance = VALUES(distance)

    """

    try:
        for route in routes:
            cursor.execute(
                query,
                (
                    route["ServiceNo"],
                    route["Direction"],
                    route["StopSequence"],
                    route["BusStopCode"],
                    route["Distance"]
                )
            )
        print(f"committing {len(routes)}")
        conn.commit()

    except Exception as e:
        conn.rollback()
        print(e)
        raise

    finally:
        cursor.close()
        conn.close()

insert_bus_routes(routes)