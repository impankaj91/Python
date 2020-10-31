#Check Prime Number.
number=int(input("Enter The Number :"))
prime=True
for i in range(2,number):
    if(number%i==0):
        prime=False
        break   
if prime:
    print("Number is Prime.")
else:
    print("Number is not Prime.")
        