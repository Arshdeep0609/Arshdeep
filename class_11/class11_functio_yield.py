def demo_yield():
    print("code segment 1 executed")
    yield 1
    print("code segment 2 executed")
    yield 2
    print("code segment 3 executed")

if __name__=="__main__":
    x=demo_yield()
    print(next(x))
    print(next(x))
    print(next(x))
