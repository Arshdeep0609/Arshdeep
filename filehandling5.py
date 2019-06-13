fo=open(r"c:\python\student.txt","r")
str1=fo.read()
fo.close()

fo1=open(r"c:\python\student1.txt","w")
fo1.write(str1)
fo1.close()

print("work done")

###closed opened file
