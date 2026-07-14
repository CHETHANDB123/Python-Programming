a=99
print(a)
addr=id(a)
print(addr)

age=81
weight=81
print(id(age))
print(id(weight))

x=hex(age) #hex=show address of variable x
print(x)

#import=29 #error
import keyword
print(keyword.kwlist)

y=100
z=hex(y)
u=id(z)
print(u)
