filename=r'student.txt'
for line in open(filename):
    str1=line[:-1]
    print('string is:',str1)
    words=str1[:-1].split('|')
    print(words)
    if words[-1][-1]=='\n':
        words[-1]=words[-1][:-1]
        print(words)
        print('-'*30)
        #print(str1)
