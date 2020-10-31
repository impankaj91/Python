with open('poem.txt','r') as f:
    a=f.read()
in_word=input("Enter The Word You Want To Find :")
if(in_word in a):
    print(f"{in_word} is Present.")
else:
    print(f"{in_word} is not Present.")