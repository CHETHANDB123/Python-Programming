#Zip Function
l1=[2,4,6,8]
l2=[20,40,60,80]
zip_obj=zip(l1,l2)
print(zip_obj)
#print(list(zip_obj))
print(dict(zip_obj))

name=['a','b','c','d']
marks=[1,2,3,4]
print(list(zip(name,marks)))


#dict comprehension along with zip()
name=['a','b','c','d']
marks=[1,2,3,4]
zo=zip(name,marks)
dict_zip={k:v for k,v in zo}
print(dict_zip)

#
marks1=[5,76,45]
zo1=zip(name,marks1)
m1={k:('Pass' if v>35 else 'Fail') for k,v in zo1}
print(m1)
