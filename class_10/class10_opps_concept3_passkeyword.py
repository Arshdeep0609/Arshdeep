class A:
    pass
class B:
    pass
class Employee(A,B):
    empCount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount+=1
    def displayCount(self):
        print("total Employee %d"%Employee.empCount)
    def displayEmployee(self):
        print("name:",self.name,",Salary:",self.salary)
if __name__=="__main__":
    print("Epmloyee.__doc__:",Employee.__doc__)
    print("Epmloyee.__name__:",Employee.__name__)
    print("Epmloyee.__module__:",Employee.__module__)
    print("Epmloyee.__bases__:",Employee.__bases__)
    print("Epmloyee.__dict__:",Employee.__dict__)
    
