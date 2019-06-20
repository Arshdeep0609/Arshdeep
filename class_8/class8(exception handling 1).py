num1=int(input("enter a number:"))
num2=int(input("enter a number:"))
try:
    res=num1/num2 #execute with num2=non zero and zero
except:
    print("Divsion by zero not allowed")

    
else:
    print(num1,'/',num2,'=',res)

print("thanks")    
