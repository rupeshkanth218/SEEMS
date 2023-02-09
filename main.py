import mysql.connector
import pytuya 
from first_draft import establish_database_connection, load_existing_devices
from first_draft import Device
import time

print("Establishing connection. Please Wait.")
while True:
    try:
        db  = establish_database_connection(username="root", paswd="11223344", db_name= "exampledb")
    except Exception as e:
        print(e)
        print("Establishing connection. Please Wait.")
    else:
        print("Database connection Established.")
        break


# monitoring_devices = [Device('05200269dc4f22855fcf', '192.168.1.7',"device1"),]
monitoring_devices= []
results = load_existing_devices(db, "InstalledDevices")
print(results)
for result in results:
    monitoring_devices.append(Device(result[1],result[2],result[3]))
for device in monitoring_devices:
    device.initialize_device_connection()

for i in range(100):
    for device in monitoring_devices:
        device.data_logging(db)
        time.sleep(5)




