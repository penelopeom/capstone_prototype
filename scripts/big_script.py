import os
import mysql.connector

mydb = mysql.connector.connect( # add proper credentials
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT type FROM table WHERE result=null")

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

