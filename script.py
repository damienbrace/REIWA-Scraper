from multiprocessing import connection
from sqlite3 import Cursor
from urllib import response
import requests
from bs4 import BeautifulSoup
import psycopg2

response = requests.get("https://reiwa.com.au")
html = response.text
soup = BeautifulSoup(html, 'html.parser')

noOfHouses = soup.find("div", {"class": "homeSearch-propertyCounts"}).text.split()[0]

try:
    conn = psycopg2.connect(
    host = "139.59.116.103",
    database = "real_estate",
    user = "postgres"
    )

    cursor = conn.cursor()

    postgres_insert_query = """ INSERT INTO homes (no_of_houses) VALUES (%s)"""
    record_to_insert = noOfHouses
    cursor.execute(postgres_insert_query, record_to_insert)
    conn.commit()
    count = cursor.rowcount
    print(count, "Record inserted successfully into table")


except (Exception, psycopg2.Error) as error:
    print("Failed to insert record into mobile table", error)


finally:
    if conn:
        cursor.close()
        conn.close()
        print("Postgresql connection is closed")

print(noOfHouses.text.split()[0])