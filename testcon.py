import os
import requests
from dotenv import load_dotenv
import mysql.connector

#env variables
load_dotenv()
API_KEY = os.getenv("LTA_API_KEY")

if not API_KEY:
    raise RuntimeError("go get an API key and put into .env")

def conn_db():
    return mysql.connector.connect(
        host = os.getenv("MYSQL_HOST"),
        port = int(os.getenv("MYSQL_PORT")),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_ROOT_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE")
    )


conn = conn_db()

cursor = conn.cursor()

cursor.execute("SELECT DATABASE(), @@hostname, @@port")

print(cursor.fetchone())

cursor.execute("SHOW TABLES")

print(cursor.fetchall())

cursor.close()
conn.close()