l=[1,2,3]
print(id(l))
l[0]="a"
print(id(l))

t=(l,"ABC")
print(id(t))
l[0]=333
print(id(t))
t[0][1]=22
print(t)

a=1
print("a:",a,id(a))
b=a
print("b:",b,id(b))
a=2
print("a:",a,id(a))
print("b:",b,id(b))
