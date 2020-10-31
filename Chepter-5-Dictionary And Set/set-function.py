set_values=set() # Empty Set.
print(type(set_values)) 
set_values.add(1) #Add Value in Set.
set_values.add(2) #Add Value in Set.
set_values.add(1) #Add Value in Set.No Duplicate In O/P
set_values.add((1,2)) #Add Value in Set.
set_values.add('1') #Add Value in Set.
# Dictionary And List Cannot Add , Throw Error.
print('Length Of Set : ',len(set_values))
print(set_values)
set_num=set()
set_num.add(1)
set_num.add(2)
print('Join The Both Set :',set_values.union(set_num))
print('Common in The Both Set',set_values.intersection(set_num))

