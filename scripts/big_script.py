import os
import mysql.connector

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
    type = x[1].strip()
    address = x[2].strip()

    os.system("python3 scripts/" + type + ".py " + address)


