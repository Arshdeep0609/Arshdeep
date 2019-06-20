def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

print("factorial of 3:",factorial(3))
print("factorial of 3:",factorial(100))
