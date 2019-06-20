class A:
    def first_method(self):
        print("method of class A..")
class B(A):
    def first_method(self):
        print("method of class B..")
        super().first_method()

if __name__=="__main__":
    ob=B()
    ob.first_method()
