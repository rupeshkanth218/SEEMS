import mysql.connector
import pytuya; 
import time; 

d = pytuya.OutletDevice('05200269dc4f22855fcf', '192.168.1.10', '12345678') 
mydb = mysql.connector.connect(host = "localhost",
                               user = "root",
                               password = "raspberry", database = "exampledb")
mycursor = mydb.cursor()

sql = "INSERT INTO powerMeasurement1(power) VALUES (%s)"
for i in range(5):
    try:
        data1 = d.status()
    except TimeoutError : 
        pass 
    except ConnectionResetError : 
        pass 
    except ConnectionAbortedError: 
        pass 
    else:
        val = (int(data1['dps']['5']),)
        mycursor.execute(sql,val)
        mydb.commit()
        time.sleep(2)


