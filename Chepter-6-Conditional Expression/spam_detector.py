text=input("Enter The Text Message:\n")
#For Exmple Spam Words Are make money , click this , subscribe this.
if("make money" in text):
    spam=True
elif("click this" in text):
    spam=True
elif("subscribe this" in text):
    spam=True
else:
    spam=False
if(spam):
    print("This is a spam message. Be Aware")
else:
    print("Go Ahead, This is not a spam")