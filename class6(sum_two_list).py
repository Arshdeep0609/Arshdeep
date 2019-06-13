x=[2,3,4,5]
y=[-1,2,-2,1]
print("x:",x)
print("y:",y)
res=[]
for i,j in zip(x,y):
    res.append(i+j)
print("res:",res)    
