Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=list()
>>> y=[]
>>> type(y)
<class 'list'>
>>> z=list('Scholars')
>>> type(z)
<class 'list'>
>>> print(x)
[]
>>> print(y)
[]
>>> print(z)
['S', 'c', 'h', 'o', 'l', 'a', 'r', 's']
>>> p=['python',45.8,99,'C']
>>> p
['python', 45.8, 99, 'C']
>>> type(p)
<class 'list'>
>>> q=[11,12,13,14,15]
>>> p=['python',45.8,99,'C']
>>> type(p)
<class 'list'>
>>> p.append(12)
>>> print(p)
['python', 45.8, 99, 'C', 12]
>>> p.append('java')
>>> print(p)
['python', 45.8, 99, 'C', 12, 'java']
>>> p.append(45.8)
>>> print(p)
['python', 45.8, 99, 'C', 12, 'java', 45.8]
>>> p.append([15,12,45,'hello'])
>>> print(p)
['python', 45.8, 99, 'C', 12, 'java', 45.8, [15, 12, 45, 'hello']]
>>> p[0]
'python'
>>> p[1]
45.8
>>> p[2]
99
>>> p[3]
'C'
>>> p[8]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    p[8]
IndexError: list index out of range
>>> p[7]
[15, 12, 45, 'hello']
>>> p[-1]
[15, 12, 45, 'hello']
>>> p[-2]
45.8
>>> p[-1][0]
15
>>> p[-1][-1]
'hello'
>>> p[-1][-2]
45
>>> print(p)
['python', 45.8, 99, 'C', 12, 'java', 45.8, [15, 12, 45, 'hello']]
>>> p[1:5]
[45.8, 99, 'C', 12]
>>> p[3:7]
['C', 12, 'java', 45.8]
>>> len(p)
8
>>> p[3:len(p)]
['C', 12, 'java', 45.8, [15, 12, 45, 'hello']]
>>> p[3:len(p)-1]
['C', 12, 'java', 45.8]
>>> p
['python', 45.8, 99, 'C', 12, 'java', 45.8, [15, 12, 45, 'hello']]
>>> p[0:6]
['python', 45.8, 99, 'C', 12, 'java']
>>> p[:6]
['python', 45.8, 99, 'C', 12, 'java']
>>> p[6:8]
[45.8, [15, 12, 45, 'hello']]
>>> p[6:]
[45.8, [15, 12, 45, 'hello']]
>>> p
['python', 45.8, 99, 'C', 12, 'java', 45.8, [15, 12, 45, 'hello']]
>>> p[:]
['python', 45.8, 99, 'C', 12, 'java', 45.8, [15, 12, 45, 'hello']]
>>> p[::1]
['python', 45.8, 99, 'C', 12, 'java', 45.8, [15, 12, 45, 'hello']]
>>> p[::2]
['python', 99, 12, 45.8]
>>> 
p[::-1]
[[15, 12, 45, 'hello'], 45.8, 'java', 12, 'C', 99, 45.8, 'python']
>>> 
>>> 

>>> 

>>> 

>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> p
['python', 45.8, 99, 'C', 12, 'java', 45.8, [15, 12, 45, 'hello']]
>>> del p[2]
>>> p
['python', 45.8, 'C', 12, 'java', 45.8, [15, 12, 45, 'hello']]
>>> del p[-1]
>>> p
['python', 45.8, 'C', 12, 'java', 45.8]
>>> del p[1:4]
>>> p
['python', 'java', 45.8]
>>> p[-1]='php'
>>> p
['python', 'java', 'php']
>>> p
['python', 'java', 'php']
>>> p[-2]=90
>>> p
['python', 90, 'php']
>>> p.append('java')
>>> p.append('java')
>>> p
['python', 90, 'php', 'java', 'java']
>>> p.count('java')
2
>>> p.clear()
>>> p
[]
>>> p=['python',45.8,99,'C']
>>> p
['python', 45.8, 99, 'C']
>>> q=p
>>> q
['python', 45.8, 99, 'C']
>>> del q[-1]
>>> q
['python', 45.8, 99]
>>> p
['python', 45.8, 99]
>>> q=p.copy
>>> q
<built-in method copy of list object at 0x0228A080>
>>> q=p.copy()
>>> q
['python', 45.8, 99]
>>> p
['python', 45.8, 99]
>>> del q[-1]
>>> q
['python', 45.8]
>>> p
['python', 45.8, 99]
>>> p.extend([11,12,13,'c','c++'])
>>> p
['python', 45.8, 99, 11, 12, 13, 'c', 'c++']
>>> p.count('vips')
0
>>> p.extend(11)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    p.extend(11)
TypeError: 'int' object is not iterable
>>> p
['python', 45.8, 99, 11, 12, 13, 'c', 'c++']
>>> p.index(11)
3
>>> p.index('java')
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    p.index('java')
ValueError: 'java' is not in list
>>> p.insert('php',0)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    p.insert('php',0)
TypeError: 'str' object cannot be interpreted as an integer
>>> p.insert(0,'php')
>>> p
['php', 'python', 45.8, 99, 11, 12, 13, 'c', 'c++']
>>> p.insert(4,'perl')
>>> p
['php', 'python', 45.8, 99, 'perl', 11, 12, 13, 'c', 'c++']
>>> p.insert(24,'perk')
>>> p
['php', 'python', 45.8, 99, 'perl', 11, 12, 13, 'c', 'c++', 'perk']
>>> p.insert('perl')
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    p.insert('perl')
TypeError: insert() takes exactly 2 arguments (1 given)
>>> p
['php', 'python', 45.8, 99, 'perl', 11, 12, 13, 'c', 'c++', 'perk']
>>> p.index('perl',2)
4
>>> p.pop()
'perk'
>>> x=p.pop()
>>> x
'c++'
>>> p
['php', 'python', 45.8, 99, 'perl', 11, 12, 13, 'c']
>>> p.pop(3)
99
>>> p
['php', 'python', 45.8, 'perl', 11, 12, 13, 'c']
>>> p.remove('python')
>>> p
['php', 45.8, 'perl', 11, 12, 13, 'c']
>>> p.pop(7)
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    p.pop(7)
IndexError: pop index out of range
>>> p.remove('python')
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    p.remove('python')
ValueError: list.remove(x): x not in list
>>> p.pop(p.index('perl'))
'perl'
>>> p
['php', 45.8, 11, 12, 13, 'c']
>>> p[0]
'php'
>>> p.reverse()
>>> p
['c', 13, 12, 11, 45.8, 'php']
>>> p=p[::-1]
>>> p
['php', 45.8, 11, 12, 13, 'c']
>>> del p[1:5]
>>> p
['php', 'c']
>>> p.sort()
>>> p
['c', 'php']
>>> p.sort(reverse=True)
>>> p
['php', 'c']
>>> p=['php','php','perl','c','perl','perl']
>>> max(p)
'php'
>>> min(p)
'c'
>>> set(p)
{'c', 'php', 'perl'}
>>> max(set(p),key=p.count)
'perl'
>>> 
