import random
random_value=random.randint(1,50)
#print(random_value)
user_input=None
guess=0
while(user_input!=random_value):
    guess+=1
    user_input=int(input("Please Guess One Value:"))
    if(user_input==random_value):
        print("You Guess Right.")
    else:
        if(user_input>random_value):
            print("Please Try Smaller Number :(")
        else:
            print("Please Try Large Number :(")

print(f"No of Try You Take = {guess}")
with open('highscore.txt','r') as f:
    score=f.read()
if(guess < int(score)):
    print("Hurray You Broke Highscore.")
    with open('highscore.txt','w') as f:
        f.write(str(guess))
else:
    print("Please Try To High.")