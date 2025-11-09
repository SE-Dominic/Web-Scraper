import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
#SQLite will be the database

#request requires url for access

#could get status code
#STATUS CODES#
#200 = OK, 202 = ACCEPTED, 204 = NO CONTENT, 302 = TEMPORARY REDIRECT
#400 = BAD REQUEST, 401 = UNAUTHORIZED, 404 = NOT FOUND, 408 = REQUEST TIMED OUT
# 500 = INTERNAL SERVER ERROR, 502 = BAD GATEWAY, 504 = GATEWAY TIMEOUT
try:
    response = requests.get("https://www.google.com")
    if response.status_code == 200:
        print(f"Successful entry to link. Status code: {response.status_code}")
        soup = BeautifulSoup(response.text, "html.parser") #creates a parser for the link provided
        #find first heading using the find function
        div = soup.find("div")
        print(div.get_text(strip=True))
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")