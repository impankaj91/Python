#Author : Pankaj Shah
#Date : 22-10-2020
name = "Pankaj Shah"
print("Name :"+name,";Type:",type(name))
# implement string function.
string_lenght=len(name) #len(variablename) find lenght of string.
print("Lenght Of String:",string_lenght)
print(name.endswith("Shah"))
print("Number of a :",name.count('a')) 
updatename=name.replace("Pankaj","PANKAJ") # replace(old,new)
print(updatename)
print(name.find(" ")) # Find A single Space.
print(updatename.capitalize())

