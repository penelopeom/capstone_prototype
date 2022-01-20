import os
import mysql.connector

mydb = mysql.connector.connect( # add proper credentials
  host="soccerdb.calingaiy4id.us-east-2.rds.amazonaws.com",
  user="njccic_usr",
  password="iJdf56*kf",
  database="njccic_capstone"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT request_type FROM requests WHERE result is null")

myresult = mycursor.fetchall()

for x in myresult: # pretend the scripts genuinely exist
    if x.equals("contact"):
        os.system("python3 contact.py")
    elif x.equals("geolocation"):
        os.system("python3 geolocation.py")
    elif x.equals("nslookup"):
        os.system("python3 nslookup.py")
    elif x.equals("overview"):
        os.system("python3 overview.py")
    elif x.equals("socials"):
        os.system("python3 socials.py")

