import os
from pip._internal import main
main(['install','mysql-connector-python'])
from pip._internal import main
main(['install', 'python-whois'])
import mysql.connector
from whois import *

mydb = mysql.connector.connect( # add proper credentials
  host="soccerdb.calingaiy4id.us-east-2.rds.amazonaws.com",
  user="njccic_usr",
  password="iJdf56*kf",
  database="njccic_capstone"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT request_id, request_type, address FROM requests WHERE result is null")

myresult = mycursor.fetchall()

for x in myresult: # pretend the scripts genuinely exist
    print(x)
    id = x[0]
    type = x[1].strip()
    address = x[2].strip()

    mycursor.execute("UPDATE requests SET result = 'PENDING' WHERE request_id = " + str(id))

    results = whois(address)
    print(results)

    mycursor.execute("UPDATE requests SET result = " + results + " WHERE request_id = " + str(id))



