import os

from pip._internal import main
main(['install','mysql-connector-python'])
from pip._internal import main
main(['install', 'ipwhois'])
from pip._internal import main
main(['install', 'python-dotenv'])

from ipwhois import IPWhois
from dotenv import load_dotenv
import mysql.connector

import whois_script
import nslookup_script
import geolocation_script

load_dotenv()
HOST = os.environ.get("HOST")
USER = os.environ.get("USER")
PASSWORD = os.environ.get("PASSWORD")
DATABASE = os.environ.get("DATABASE")

mydb = mysql.connector.connect( # add proper credentials
  host=HOST,
  user=USER,
  password=PASSWORD,
  database=DATABASE
)

mycursor = mydb.cursor()

mycursor.execute("SELECT request_id, request_type, address FROM requests WHERE result = ''")

myresult = mycursor.fetchall()

for x in myresult: # pretend the scripts genuinely exist
    print(x)
    id = x[0]
    type = x[1].strip()
    address = x[2].strip()

    mycursor.execute("UPDATE requests SET result = 'PENDING' WHERE request_id = \"" + id + "\" and address = \"" + address + "\"")
    
    if (type == "whois"):
      results = whois_script.whois_func(address)
    elif (type == "nslookup"):
      results = nslookup_script.nslookup_func(address)
    elif (type == "geolocation"):
      results = geolocation_script.geolocation_func(address)
    elif (type == "all"):
      whois_results = (whois_script.whois_func(address)).strip()
      nslookup_results = nslookup_script.nslookup_func(address).strip()
      geo_results = geolocation_script.geolocation_func(address)
      results = whois_results + "; \n" + nslookup_results + "; \n" + geo_results
    
    print(results)

    mycursor.execute("UPDATE requests SET result = \"" + results + "\" WHERE request_id = \"" + id + "\" and address = \"" + address + "\"")
    mydb.commit()



