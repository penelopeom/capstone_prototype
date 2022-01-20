import os
import mysql.connector

mydb = mysql.connector.connect( # add proper credentials
  host="soccerdb.calingaiy4id.us-east-2.rds.amazonaws.com",
  user="njccic_usr",
  password="iJdf56*kf",
  database="njccic_capstone"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT request_id, request_type FROM requests WHERE result is null")

myresult = mycursor.fetchall()

for x in myresult: # pretend the scripts genuinely exist
    print(x)
    type = x[0].strip()

    if type.equals("contact"):
        os.system("python3 contact.py")
    elif type.equals("geolocation"):
        os.system("python3 geolocation.py")
    elif type.equals("nslookup"):
        os.system("python3 nslookup.py")
    elif type.equals("overview"):
        os.system("python3 overview.py")
    elif type.equals("socials"):
        os.system("python3 socials.py")

