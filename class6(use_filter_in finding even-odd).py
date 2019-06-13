#filter() filters an iterable by removing items that don't match a predicate
#predicate is a function that returns a boolean
def find_odd(x):
    if x%2==1:
        return True
    else:
        return False
def find_even(x):
    if x%2==0:
        return True
    else:
        return False
    
nums=[11,22,33,44,55]
result=list(filter(find_odd,nums))
print(nums)
print("odd:",result)
print('-'*20)
num=[11,22,33,44,55]
result=list(filter(lambda x:x%2==1,num))
print("odd:",result)
print('-'*20)
result=list(filter(lambda x:x%2==0,num))
print("even:",result)
print('-'*20)
result=list(filter(find_even,nums))
print(nums)
print("even:",result)
