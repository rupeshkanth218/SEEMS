# Example Usage of TinyTuya
import tinytuya
import time

d = tinytuya.OutletDevice('d7e6ab37bac96c17aax3zf', '192.168.1.9', '6338ab55ad963843')
e=tinytuya.OutletDevice('05200269dc4f22855fcf', '192.168.1.22', 'a30de588a3bf1886')
d.set_version(3.3)
e.set_version(3.1)
#d.set_value(1,True)
for i in range(20):
	data = e.status() 

	print('Device status: %r' % data)
	time.sleep(1)

#data = d.status() 

#print('Device status: %r' % data)