#Loop Controling Statement
#break
'''
for i in range(1,11):
    if i==7:
        break
    print(i)


for i in range(1,11):
    if i%4==0:
        break
    print(i)

l=[23,42,11,56,32,-4,6,-6,-7]
for i in l:
    if i<0:
        break
    print(i)

d={1:10,2:20,3:30,4:40} #dict
for i in d.items():
    print(i)
    
s="abc"   #str
for i in s: #Each character is iterated/traversed
    print(i)
'''
'''
#continue
for i in range(1,11):
    if i==7:
        continue
    print(i)
    
for i in range(1,11):
    if i%4==0:
        continue
    print(i)

l=[11,20,-3,4,100,-11,23,79]
for i in l:
    if i<0:
        continue
    print(i)

#pass
for i in range(1,22):
    pass
#nested for
for i in range(1,3):
    for j in range(6,8):
        print(i,j)

for i in range(7,10):
    for j in range(1,4):
        r=i*j
        #print(f"{i}*{j}={r}")
        print(f"{i}*{j}={i*j}")
'''
#else-for
l=[23,1,34,4,6,7,3]
for i in l:
    if i==6:
        print("roll number found",i)
        break
else:
    print("roll number not found")
    


















