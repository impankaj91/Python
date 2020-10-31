def p_star(n):
    for i in range(n):
        print("*" * (n-i))       


number=int(input('Enter The Number :'))
if number>0:
    p_star(number)
else:
    print("Please , Be Positive.")