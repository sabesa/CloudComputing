import time
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()
while True:
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        conn.close()
        print("Database is ready!")
        break
    except psycopg2.OperationalError:
        print("Waiting for database...")
        time.sleep(2)
