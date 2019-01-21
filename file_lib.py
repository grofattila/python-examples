def file_ir(filenev):
	f = open(filenev, "w") 
	tartalom = f.write("Hello from the python side.") 
	f.close() 

def file_folytat(filenev, data):
	f = open(filenev, "a") 
	tartalom = f.write(data) 
	f.close() 

def file_olvas(filenev):
	f = open(filenev, "r") 
	tartalom = f.read() 
	f.close()
	print(tartalom)
