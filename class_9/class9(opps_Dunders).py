class Complex:
    def __init__(self,real,image):
        self.real=real
        self.image=image
    def __add__(self,ob):
        return Complex(self.real+ob.real,self.image+ob.image)
    def __sub__(self,other):
        return Complex(self.real-other.real,self.image-other.image)
    def __str__(self):
        return str(self.real)+"+"+str(self.image)+"j"

z1=Complex(5,7)
z2=Complex(3,8)
z3=z1+z2
print(z3.real)
print(z3.image)
print(z3)
z3=z1-z2
print(z3.real)
print(z3.image)
print(z3)
        
