import mysql.connector
import pytuya 
from first_draft import establish_database_connection, load_existing_devices
from first_draft import Device

print("Establishing connection. Please Wait.")
while True:
    try:
        db, cursor = establish_database_connection(username="root", paswd="raspberry", db_name= "exampledb")
    except:
        print("Establishing connection. Please Wait.")
    else:
        print("Database connection Established.")
        break


monitoring_devices = [Device('05200269dc4f22855fcf', '192.168.1.10'),]

for device in monitoring_devices:
    device.initialize_device_connection()




