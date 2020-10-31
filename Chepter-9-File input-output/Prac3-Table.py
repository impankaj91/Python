#Print Tables 2 to 20 in diffrent files in table folder.
for i in range(2,21):
    with open(f"table/table of_{i}.txt",'w') as f:
        for j in range(1,11):
            f.write(f"{i} X {j} = {i*j}\n")