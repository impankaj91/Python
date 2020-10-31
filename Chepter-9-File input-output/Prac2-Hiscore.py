#Update The High Score In hiscore.txt file Every Time if enter value big than value in text file.
def game(n):
    return n

n=int(input("Try Your fav Number To Enter In Hiscore Text :"))
score=game(n)
with open('hiscore.txt','r') as f:
    hiscore=f.read()

if hiscore == '':
    with open('hiscore.txt','w') as f:
        f.write(str(score))
elif int(hiscore)<score:
    with open('hiscore.txt','w') as f:
        f.write(str(score))
