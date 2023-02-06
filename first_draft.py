import mysql.connector
import pytuya; 
import time; 

def establish_database_connection(username="root", paswd="raspberry", db_name= "exampledb"):
    mydb = mysql.connector.connect(host = "localhost",
                               user = username,
                               password = paswd, database = db_name)
    mycursor = mydb.cursor()
    
    return mydb, mycursor

class Network:
    def __init__(self):
        return
    

class Device:
    
    def __init__(self,device_Id,device_Ip,device_Key='12345678'):
        self.device_Id=device_Id
        self.device_Ip=device_Ip
        self.device_Key=device_Key
        self.device = None
        
    def establish_device_connection(pass):
        try:
            self.device= pytuya.OutletDevice(self.device_Id,self.device_Ip,self.device_Key)
            
        except:
            print("Device Connection Failed. Please try again.")
            return None
    
    def data_logging(self, db, cursor):
        cmd = "INSERT INTO powerMeasurement1(power) VALUES (%s)"
        data = self.device.status()
        val = (int(data1['dps']['5']),)
        cursor.execute(cmd,val)
        db.commit()
        
        






