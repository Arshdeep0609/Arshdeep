num1=int(input("enter a number:"))
num2=int(input("enter a number:"))
try:
    res=num1/num2 #execute with num2=non zero and zero
except ZeroDivisionError as ob:
    print(ob)

    
else:
    print(num1,'/',num2,'=',res)
finally:
    print("resource deallocated")

print("thanks")    
