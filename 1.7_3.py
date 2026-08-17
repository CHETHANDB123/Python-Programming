#Copy_operation
#1) General copy
'''
l1=[10,20,30,[40,50]]
l2=l1 #general copy
print(l2) 
l2[2]=11 #outer list
print(l2)
l2[3][0]=41 # inner list
print("l1",l1)
print("l2",l2)

#2)shallow copy
import copy #step1 import copy module
l1=[10,20,30,[40,50]]
l2=copy.copy(l1) #shallow copy

l1[2]=11  #outer list , only l1 affected
print(l1)
print(l2)
l2[3][0]=41 #inner list(nested),both are affected
print(l2)
print(l1)
'''
#Deep copy
import copy #step1 import copy module
l1=[10,20,30,[40,50]]
l2=copy.deepcopy(l1) #deep copy

l1[2]=11  #outer list 
print(l1) #l1 will affected
print(l2) #l2 not affected
l2[3][0]=41 #inner list(nested),
print(l2) # l2 affected
print(l1) # l1 not affected
