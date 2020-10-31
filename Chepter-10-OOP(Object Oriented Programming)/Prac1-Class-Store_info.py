class Programmer:
    def store(self):
        with open("prac1_employee_data.txt","a") as f:
            f.write(f"Hello, Name is {self.name} and Salary is {self.salary}. City:{self.city}\n")
            


###For Employee
emp=Programmer()
name=input("Enter The Name:")
salary=int(input("Salary:"))
city=input("City:")
emp.name=name
emp.salary=salary
emp.city=city
emp.store()

