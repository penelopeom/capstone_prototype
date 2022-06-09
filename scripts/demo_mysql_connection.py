# this script checks if you have mysql installed and running properly :)
import mysql.connector

mydb = mysql.connector.connect(
  host="soccerdb.calingaiy4id.us-east-2.rds.amazonaws.com",
  user="njccic_usr",
  password="iJdf56*kf",
  database="njccic_capstone"
)

print(mydb)