class Employee:#Parent 1
    company="Facebook"
class Person:#parent 2
    city="Pune"
class devloper(Employee,Person):#child class.
    print("Hello I am Devloper.")

dev=devloper()
print(f"My Company is {dev.company} and I am from {dev.city}.")