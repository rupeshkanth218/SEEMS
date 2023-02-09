import mysql.connector
import pytuya 
import time



def establish_database_connection(username="root", paswd="raspberry", db_name= "exampledb"):
    mydb = mysql.connector.connect(host = "localhost",
                               user = username,
                               password = paswd, database = db_name)
    
    
    return mydb

def checkTableExists(dbcon, tablename):
    dbcur = dbcon.cursor()
    dbcur.execute("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{0}'
        """.format(tablename.replace('\'', '\'\'')))
    if dbcur.fetchone()[0] == 1:
        dbcur.close()
        return True

    dbcur.close()
    return False

def load_existing_devices(db, devices_table_name):
    cursor = db.cursor()
    cmd = f"SELECT * FROM {devices_table_name}"
    cursor.execute(cmd)
    results = cursor.fetchall()
    cursor.close()
    return results

class Device:
    
    def __init__(self,device_Id,device_Ip,tablename,device_Key='12345678',):
        self.device_Id=device_Id
        self.device_Ip=device_Ip
        self.device_Key=device_Key
        self.tablename = tablename
        self.device = None
        
    def initialize_device_connection(self):
        try:
            self.device= pytuya.OutletDevice(self.device_Id,self.device_Ip,self.device_Key)
            return True
        except:
            print("Device Connection Failed. Please try again.")
            return None
    
    def data_logging(self, db):
        try:
            data = self.device.status()
        except TimeoutError:
            return
        except ConnectionResetError : 
            return
        except ConnectionAbortedError: 
            return 
        except TypeError:
            return
        else:
            cursor = db.cursor()
            cmd = f"INSERT INTO {self.tablename}(power) VALUES (%s)"
            
            val = (int(data['dps']['5']),)
            cursor.execute(cmd,val)
            cursor.close()
            db.commit()
            print("Write Complete.")
        






