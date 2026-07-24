#slicing
l=[10,20,30,40,50,60,70,80]
l1=l[0]
print(l1)
l2=l[-1]
print(l2)
sl=l[0:4:2]
print(sl)
sl2=l[3:7:1]
print(sl2)
sl3=l[4::]
print(sl3)
print(l[::])

print(l[0:7:2])
print(l[:7:2])
print(l[::3])

#reverse
rl=[1,2,3,4,5,6,7,8]
r1=rl[-1]
print(r1)
r2=rl[6:3:-1]
print(r2)
r3=rl[-2:-5:-1]
print(r3)

s='good'#string
print(s[-1:-5:-1])
s1="i am chethan"
print(s1[0:6:1])

s3=(1,2,3,4,5)#Tuple
print(s3[2:4:1])
print(s3[-1:-5:-2])
#slice the string starting from 2nd occurance of 'a'
s4='aryabhatta'
print(s4[3:])
soccur_index=s4.index('a',1)
print(soccur_index)
print(s4[soccur_index::])

#Negative slicing
#Reverse slicing use negative step
print(s4[-1::-1])
print(s4[::-1])
l=[10,20,30,40,50,60,70,80]
rl=l[-2:-4:-1]
print(rl)

rl2=l[-2:-len(l)-1:-2] #-Exclusive
print(rl2)

rl3=l[6:3:-1]
print(rl3)
