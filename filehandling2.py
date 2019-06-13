fo=open(r"c:\python\student.txt","w")#a
str1=input("enter.txt:")
x=fo.write(str1)
print("no of bytes written:",x)
fo.write('\nwe are using file handling')
fo.close()
print("work done")           
           
