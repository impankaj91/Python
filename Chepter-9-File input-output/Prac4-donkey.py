#Replace A donkey Word With #####
with open("donkey.txt","r") as f:
    data=f.read()

if 'Donkey' in data:
    with open("donkey.txt","w") as f:
        f.write(data.replace('Donkey','#####'))
