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
    type = x[1].strip()
    print(type)

    if type == "contact":
        os.system("python3 scripts/contact.py")
    elif type == "geolocation":
        os.system("python3 scripts/geolocation.py")
    elif type  == "nslookup":
        os.system("python3 scripts/nslookup.py")
    elif type == "overview":
        os.system("python3 scripts/overview.py")
    elif type == "socials":
        os.system("python3 scripts/socials.py")
    else:
        print("LLLLLL stoopid")

