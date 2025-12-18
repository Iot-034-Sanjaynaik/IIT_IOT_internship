# import mysql connector
import mysql.connector

# establish connection with mysql server
connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="smart_agriculture",
    use_pure=True
)

# take input from user
Sensor_ID = int(input("Enter sensor id : "))
Moisture_level = float(input("Enter moisture level : "))
Date_and_Time = input("Enter date and time (YYYY-MM-DD HH:MM:SS) : ")

# form insert query
insert_query = f"""
INSERT INTO soil_moisture  
VALUES ({Sensor_ID}, {Moisture_level}, '{Date_and_Time}');
"""

# create cursor
cursor = connection.cursor()

# execute insert query
cursor.execute(insert_query)

# commit changes
connection.commit()

cursor.close()
connection.close()