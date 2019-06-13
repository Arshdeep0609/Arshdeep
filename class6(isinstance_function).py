x=['python','java',88,99,99.9,'c++','perl','adda']
def fun_str(a):
    if isinstance(a,str):
        return a
    
y=list(filter(fun_str,x))
z=list(filter(lambda a:isinstance(a,int),x))
p=list(filter(lambda a:isinstance(a,(int,float)),x))
print(y)
print(z)
print(p)
