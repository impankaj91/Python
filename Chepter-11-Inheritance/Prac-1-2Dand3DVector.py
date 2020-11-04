class C2dvector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def __str__(self):
        if(self.i<0 and self.j<0 ):
            return f"{self.i}i {self.j}j"
        elif(self.i<0 and self.j>0):
            return f"{self.i}i + {self.j}j"
        elif(self.i>0 and self.j<0):
            return f"{self.i}i {self.j}j"
        elif(self.i>0 and self.j>0):
            return f"{self.i}i + {self.j}j"

class C3dvector(C2dvector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k
    def __str__(self):
         if(self.i>0 and self.j>0 and self.k>0):
            return f"{self.i}i+{self.j}j+{self.k}k"
         elif(self.i>0 and self.j>0 and self.k<0):
            return f"{self.i}i + {self.j}j {self.k}k"
         elif(self.i>0 and self.j<0 and self.k>0):
            return f"{self.i}i  {self.j}j + {self.k}k"
         elif(self.i>0 and self.j<0 and self.k<0):
            return f"{self.i}i {self.j}j {self.k}k"
         elif(self.i<0 and self.j>0 and self.k>0):
            return f"{self.i}i + {self.j}j +j{self.k}k"
         elif(self.i<0 and self.j>0 and self.k<0):
            return f"{self.i}i + {self.j}j {self.k}k"
         elif(self.i<0 and self.j<0 and self.k>0):
            return f"{self.i}i  {self.j}j + {self.k}k"
         elif(self.i<0 and self.j<0 and self.k<0):
            return f"{self.i}i  {self.j}j {self.k}k"    
        

user_input_x=int(input("Enter The X Value :"))
user_input_y=int(input("Enter The Y Value :"))
user_input_z=int(input("Enter The Z Value :"))
two_2d=C2dvector(user_input_x,user_input_y)
three_3d=C3dvector(user_input_x,user_input_y,user_input_z)
print("Your 2D Value is :" , two_2d)
print("Your 3D Value is :" , three_3d)