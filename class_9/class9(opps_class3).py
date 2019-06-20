class Dog:
    price=400
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def bark(self):
        print("woof")
        print(self.name,"has ",self.price," price and its color is ",self.color)

if __name__=="__main__":
    pet1=Dog("tommy","brown")
    pet2=Dog("sherru","white")
    pet1.bark()
    pet2.bark()
    print(pet1.x)#attribute error
    print(pet1.price)
    print(pet2.price)
    print(Dog.price)
    Dog('abc','blue').bark()
