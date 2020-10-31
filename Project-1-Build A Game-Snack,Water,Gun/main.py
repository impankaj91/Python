import random 
def gameWin(com,player):
    #Logic Of Building Game. Base On Function We get Result like Tie , Won or Loss.
    if player == comp:
        return None
    elif comp == 's':
        if player == 'w':
            return False
        elif player == 'g':
            return True
    elif comp == 'w':
        if player == 'g':
            return False
        elif player == 's':
            return True
    elif comp == 'g':
        if player == 'w':
            return True
        elif player == 's':
            return False
    
randNo=random.randint(1,3) #For Computer Random To Select Random Option Base On Number.
#print(randNo) 
if randNo == 1:
    comp='s'
elif randNo == 2:
    comp='g'
elif randNo == 3:
    comp='w'
#Take a Input From User.
player=input("For Snake Press(s) or gun(g) or water(w) : ")

#To Check User Enter Valid Input Or Not and print Result.
if(player=='s' or player=='g' or player=='w'):
    a=gameWin(comp,player)
    if a is None:
        print("Tie")
    elif a:
        print("Hurray You Won !")
    else:
        print("Sorry , You Loss !")
else:
    print("Please,Enter Valid Input.")