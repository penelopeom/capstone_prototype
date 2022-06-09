#!/usr/bin/env python
import os

from ipwhois import IPWhois
from dotenv import load_dotenv
import mysql.connector
import time

import whois_script
import nslookup_script
import geolocation_script
import contact_script

load_dotenv()
HOST = os.environ.get("HOST")
USER = "root"
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
i = 0
for x in myresult: 
  try:
    print(x)
    id = x[0]
    type = x[1].strip()
    address = x[2].strip()

    mycursor.execute("UPDATE requests SET result = 'PENDING' WHERE request_id = \"" + id + "\" and address = \"" + address + "\"")

    mycursor.execute("SELECT result FROM requests WHERE address = \"" + address + "\" and request_type = \"" + type + "\" and request_id != \"" + id + "\"")
    savedResults = mycursor.fetchall()
    if (len(savedResults) > 0):
        print("thinks we have previous results")
        results = savedResults[0][0]
    else: 
      if (type == "whois"):
        results = whois_script.whois_func(address)
      elif (type == "nslookup"):
        results = nslookup_script.nslookup_func(address)
      elif (type == "geolocation"):
        results = geolocation_script.geolocation_func(address)
      elif (type == "contact"):
        results = contact_script.contact_func_solo(address)
      elif (type == "all"):
        whois_results = (whois_script.whois_func(address)).strip()
        nslookup_results = nslookup_script.nslookup_func(address).strip()
        geo_results = geolocation_script.geolocation_func(address)
        contact_results = contact_script.contact_func_all(address, whois_results, geo_results)
        results = whois_results + "; \n" + nslookup_results + "; \n" + geo_results + "; \n" + contact_results
      else:
        print("doesn't recognize type")
  except:
    results = "Error thrown when handling request "

  print(results)

  mycursor.execute("UPDATE requests SET result = \"" + results + "\" WHERE request_id = \"" + id + "\" and address = \"" + address + "\"")
  mydb.commit()
  i += 1
  # if i % 100 = 0:
  #    time.sleep(1)





