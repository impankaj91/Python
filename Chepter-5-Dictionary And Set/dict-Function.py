#Dictionary is in form of Key-Value Pair . Access by Key.
#Fuctions Of Dictionary.
#Syntax : {'Key':'Value'}
mydict= { 'Name' : 'Pankaj' ,  'Last' : 'Shah' , 'Mark' : 784 , 1:2}
print(mydict['Name']) # Print using key 'Pankaj'.Note : Throw Error If Key Not Find.
print(mydict.get('Name')) # Print using key 'Pankaj'.Note : Throw Non Value If Key Not Find.
print(mydict.items()) # Display All Items in Dictionary.
print(mydict.keys())  # Display Keys .
print(mydict.values()) # Display Values
print(mydict.pop(1)) # Remove The Value Using Key. 
mydict.update({'Name' : 'PANKAJ'}) #Update A Value Of Key.
print(mydict.values())