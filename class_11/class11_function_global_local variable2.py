total=100

def add(arg1,arg2):
    global total
    total=arg1+arg2
    print("inside the function total:",total)
    return total
a=add(10,20)
print("outside the function global total:",total)
