
try:
    num1=int(input("enter a number:"))
    num2=int(input("enter a number:"))
except ValueError as ob:
    print(ob)
else:
    try:
        res=num1/num2 #execute with num2=non zero and zero
    except ZeroDivisionError as ob:
        print(ob)

    else:
        print(num1,'/',num2,'=',res)

print("thanks")    
