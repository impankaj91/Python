class Calculator:
    def __init__(self,num):
        self.number=num
    def square(self):
        print(f"Value Of {self.number} Square = {self.number **2}")
    def squareRoot(self):
        print(f"Value Of {self.number} SquareRoot = {self.number **0.5}")
    def cube(self):
        print(f"Value Of {self.number} Cube = {self.number **3}")
    @staticmethod
    def greet():
        print("You'r Calculation is finished.Thanks!")

n=int(input("Enter The Number:"))
value=Calculator(n)
value.square()
value.squareRoot()
value.cube()
value.greet()