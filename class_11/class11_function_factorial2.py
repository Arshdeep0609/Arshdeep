import sys

sys.setrecursionlimit(5000)

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(3000))    
