def gratest(num1,num2,num3):
    if(num1>num2):
        f=num1
    else:
        f=num2
    if(f>num3):
        return f
    else:
        return num3

num_1=int(input("Enter Number 1:"))
num_2=int(input("Enter Number 2:"))
num_3=int(input("Enter Number 3:"))
print(f"Gratest Value = {gratest(num_1,num_2,num_3)}.")