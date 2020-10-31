#Sample.txt File Read Using File I/O.
f=open('sample.txt','r') #Open Function : open("Filename","operationtype")
data=f.read() #read operation.
#data1=f.read(5) #read first 5 character.
print(data) #Print First Time.
#print(data1) #print Second Time.
f.close() #Close File.