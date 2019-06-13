##def add_five(x):
##    temp=x+5
##    return temp
##
##num=[11,22,33,44,55]
##result=list(map(add_five,num))
##print("num:",num)
##print("result:",result)

print('-'*40)
num=[11,22,33,44,55]
result=list(map(lambda x:x+5,num))
print(num)
print("After the use of lambda in map:",result)
