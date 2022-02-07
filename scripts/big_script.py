import os
from pip._internal import main
main(['install','mysql-connector-python'])
from pip._internal import main
main(['install', 'ipwhois'])
from ipwhois import IPWhois
from dotenv import load_dotenv
import whois_script
import mysql.connector

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

mycursor.execute("SELECT request_id, request_type, address FROM requests WHERE result is null")

myresult = mycursor.fetchall()

for x in myresult: # pretend the scripts genuinely exist
    print(x)
    id = x[0]
    type = x[1].strip()
    address = x[2].strip()

    mycursor.execute("UPDATE requests SET result = 'PENDING' WHERE request_id = " + str(id))

    results = whois_script.whois_func(address)
    print(results)

    mycursor.execute("UPDATE requests SET result = \"" + results + "\" WHERE request_id = " + str(id))
    mydb.commit()



