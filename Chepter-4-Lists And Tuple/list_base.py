#Author: Pankaj Shah
#Date: 25-10-2020
# List is defined by [item1 , item2 etc.].
number=[1,10,30,7,50]
print(number[0]) # Get Value From O index.
number.append(65) # Add 65 end of list
print(number.index(1)) # Location of Value 1.
number.insert(2,10) # Add Value 10 At Index 2.
number.sort() # Asecnding Order List.
number.pop(2) # value remove at index 2.
number.reverse()
number.remove(10) # remove value 10.
print(number)