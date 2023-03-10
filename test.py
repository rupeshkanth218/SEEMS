import mysql.connector
import pytuya
import time 
import json

d = pytuya.OutletDevice('d7e6ab37bac96c17aax3zf', '192.168.1.9', '6338ab55ad963843') 
d.turn_off()
print(d.status())

# for i in range(10):
#     data = d.status()
#     print(data.hex())
#     #print(json.load(data.decode()))
    
    
#     time.sleep(3)

#d = pytuya.OutletDevice('05200269dc4f22855fcf', '192.168.1.10', '12345678') 
# mydb = mysql.connector.connect(host = "localhost",
#                                user = "root",
#                                password = "raspberry", database = "exampledb")
# mycursor = mydb.cursor()

# sql = "INSERT INTO powerMeasurement1(power) VALUES (%s)"
# for i in range(5):
#     try:
#         data1 = d.status()
#     except TimeoutError : 
#         pass 
#     except ConnectionResetError : 
#         pass 
#     except ConnectionAbortedError: 
#         pass 
#     else:
#         val = (int(data1['dps']['5']),)
#         mycursor.execute(sql,val)
#         mydb.commit()
#         time.sleep(2)


