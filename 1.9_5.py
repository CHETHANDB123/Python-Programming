#Iterator
'''      #1st way
l=[1,2,3,4]
#creating an iterator obj
itr_obj=iter(l)
print(itr_obj) #Address of iteartor obj
ele1=next(itr_obj)
print(ele1)
print("chethan")
ele2=next(itr_obj)
print(ele2)
ele3=next(itr_obj)
print(ele3)
ele4=next(itr_obj)
print(ele4)
#ele5=next(itr_obj)
#print(ele5)
print(ele2)
print("__________")
#######
t=(1,2,3,4)    #2nd way
#create itarator
itr_obj=iter(t)
for i in itr_obj: #2nd way of Access iterator elements is using for loop
    print(i)
###########
'''
t=(1,2,3,4)     #3rd way
itr_obj=iter(t)   #Explicit
print(list(itr_obj))

###
r=(11,22,33,44)
itr_o=iter(r)
i=0
while i<len(r):
    print(next(itr_o))
    i+=1













