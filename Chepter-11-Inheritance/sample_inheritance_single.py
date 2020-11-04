class Student:#Parent Class
    SchoolName="R.S.S.S"
    
class Gamer(Student):#Child Class
    s_name="Pankaj"

stud=Student()
games=Gamer()
print(f"Name is {games.s_name} and Schoolname is {games.SchoolName}.")