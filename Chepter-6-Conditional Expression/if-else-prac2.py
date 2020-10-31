#Practical : Student Need To Require  Pass total 40 % and 33% for individual Subjects.
maths=int(input("Enter The Marks Of Maths :"))
chem=int(input("Enter The Marks Of Chemistry :"))
phy=int(input("Enter The Marks Of Physics :"))

total=((maths+chem+phy)/3)
if(total>40 and maths>33 and chem>33 and phy>33):
    print("Pass")
else:
    print("Fail!")