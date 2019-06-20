try:
    fh=open(r"c:\python\student5.txt","r")
    fh.write("this is my test file for exception handling!!")
except Exception as ob:
    print(ob)
finally:
    print("Error:can't find file or read data ")
    try:
        fh.close()
    except Exception as ob:
        print(ob)
print("thanks")    
