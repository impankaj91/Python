def rec_sum(number):
    if number <= 0:
        return number
    else:
        return number + rec_sum(number-1)
    
n=int(input("Enter The Number : "))
if n>0:
    print(f" sum of {n} natural number is = {rec_sum(n)} .")
else:
    print("Please , Be Positive.")