def PrintBlue():
    print('you choose blue:\n')
    return
def PrintRed():
    print('you choose red:\n')
    return
def PrintOrange():
     print('you choose orange:\n')
     return
def PrintYellow():
     print('you choose yellow:\n')
     return
def choice():
    print("0:blue")
    print("1:red")
    print("2:orange")
    print("3:yelow")
    print("4:quit")
    return
Colorselect={0:PrintBlue,1:PrintRed,2:PrintOrange,3:PrintYellow}
selection=0
while True: 
           if selection==4:break
           choice()
           selection=int(input("select color option:"))
           if(selection>=0)and(selection>4):
               Colorselect[selection]()
