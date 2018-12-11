def file_read(filename):
    '''
    Fájl megnyítása olvasásra.
    '''
    opened_file = open(filename, "r") 
    content = opened_file.read() 
    opened_file.close()
    return content

def file_ir(filenev):
    f = open(filenev, "w")
    f.write("első írás")
    f.write("\n")
    f.close()

def file_folytatas(filenev, adat_tartalom):
    f = open(filenev, "a")
    f.write(adat_tartalom)
    f.write("\n")
    f.close()
    
file_ir("pelda.txt")
file_folytatas("pelda.txt", "1 sor")
file_folytatas("pelda.txt", "2 sor")
adat = file_olvas("pelda.txt")

print(adat)

list = []

list = adat.split("\n")
print (list)
