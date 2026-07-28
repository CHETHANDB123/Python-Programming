#Type Casting
#implicit T C in singlevalued D T
#bool to other bigger dt
print(True+5) #bool->int
print(True+7.3) #bool->float
print(True+8-3j) #bool->complex

#int to bigger dt
print(3+2.2) #int->float
print(2-1+3j) #int->complex

#float to complex
print(3.3-4.2j) #float->complex

#Explicit T C in singlevalued D T smaller to bigger
b=True
i=88
f=3.3
c=3+4j
print(int(b)) #Explicit classname
print(float(b))
print(complex(b))

print(float(i))
print(complex(i))

print(complex(f))

#Explicit TC from bigger to smaller
i_b=bool(i)
print(i_b)

f_b=bool(f)
print(f_b)

c_b=bool(c)
print(c_b)

#float to int
f_i=int(f)
print(f_i) #here decimal points are negleted

#complex to int cannot be type cast
##c_i=int(c)
##print(c_i)

#complex to float cannot be type cast
#c_f=float(c)
#print(c_f)
print("========")
##Typecasting list to other multi value data types
l=[10,20,30]

l_t=tuple(l)
print(l_t)
l_s=set(l)
print(l_s)
l_str=str(l)
print(l_str,type(l_str))
#l_d=dict(l) #TypeError: object is not iterableCannot convert dictionary update sequence element #0 to a sequence
#print(l_d)

#typecasting tuple to other MV data types
t=(22,33,44)

t_l=list(t)
print(t_l)
t_s=set(t)
print(t_s)
t_str=str(t)
print(t_str,type(t_str))
#t_d=dict(t) #TypeError: object is not iterable
#print(t_d)

#type casting SET to other MV data types
s=(1,2,3,4)
s_l=list(s)
print(s_l)
s_t=tuple(s)
print(s_t,type(s_t))
s_str=str(s)
print(s_str)
#s_d=dict(s)
#print(s_d) error

#string to other MV
st='ppython'
st_l=list(st)
print(st_l)
st_t=tuple(st)
print(st_t)
st_s=set(st)
print(st_s)
##st_d=dict(st)
##print(st_d)

#Dict to other MV
d={1:100,2:200,3:300}
d_l=list(d)
print(d_l)
print(list(d.keys()))
print(list(d.values()))
d_t=tuple(d)
print(d_t)
d_s=set(d)
print(d_s)
d_str=str(d)
print(d_str)

