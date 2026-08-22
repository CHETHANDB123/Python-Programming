#lambda
'''
#1)Assign to var then call
var=lambda a,b:a+b
print(var(11,22))

var2=lambda a,b,c:a*b*c
print(var2(2,2,2))
#2)Direct call
print((lambda a,b:a+b)(11,11))
#
def square(num): #callback
    return num**2
def transform(fun,col): #HOF
    new_list=[]
    for ele in col:
        res=fun(ele) #or res= ele**2
        new_list.append(res)
    return new_list
l=[10,20,30,40]
print(transform(square,l))

#using lambda
def transform(fun,col): #HOF
    new_list=[]
    for ele in col:
        res=fun(ele) #or res= ele**2
        new_list.append(res)
    return new_list                #Important: return does not print anything. It gives the value back. print() is what displays it
l=[10,20,30,40]
print(transform(lambda num:num**2,l))
print(transform(lambda num:num**3,l))
print(transform(lambda num:num+50,l))

##Predefined HOF
#1)map function
ref=map(lambda num:num**2,[10,20,30,40])
print(ref)
print(list(ref))
#
print(list(map(lambda num:num**2,[10,20,30,40])))

#
print(list(map(lambda num:num//5,[10,20,30,40])))

print("============")
#2)Filter fun
def is_even(n): #callback/simple helper fun
    return n%2==0
def transform(fun,col):  #HOF
    nl=[]
    for ele in col:
        if fun(ele):  #or  if ele%2==0
            nl.append(ele)

    return nl
l=[11,22,33,44,55]
print(transform(is_even,l))
##
def transform(fun,col):  #HOF
    nl=[]
    for ele in col:
        if fun(ele):  #or  if ele%2==0
            nl.append(ele)

    return nl
l=[11,22,33,44,55]
print(transform(lambda n:n%2==0,l))
#
ref=filter(lambda n:n%2==0,[11,22,33,44,55])
print(list(ref))

print(list(filter(lambda n:n%2==0,[11,22,33,44,55])))
print(list(filter(lambda n:30<n<50,[11,22,33,44,55])))

print("++++++++++")
'''
#3)reduce fun
def add(n1,n2): #callback/simple helper fun
    return n1+n2
def transform(fun,col):  #HOF
    res=0
    for ele in col:
        res=fun(res,ele)  #or  res=res+ele
    return res
l=[11,22,33,44,55]
print(transform(add,l))
#
def transform(fun,col):  #HOF
    res=0
    for ele in col:
        res=fun(res,ele)  #or  res=res+ele
    return res
l=[11,22,33,44,55]
print(transform(lambda n1,n2:n1+n2,l))

#
from functools import reduce
print(reduce(lambda n1,n2:n1+n2,[11,22,33,44,55]))
#
print(reduce(lambda n1,n2:n1*n2,[2,3,4,5,1]))
#
fil_obj=filter(lambda n:n%2==0,[10,12,13,14,16,17,18])
map_obj=map(lambda a:a**2,fil_obj)
print(list(map_obj))
l=[10,12,13,14,16,17,18]
print(list(map(lambda a:a**2,filter(lambda n:n%2==0,l))))
#or

def tra(fun,col):
    li=[]
    for ele in l:
        if fun(ele):
              li.append(ele**2)
    return li
l=[10,12,13,14,16,17,18]
print(tra(lambda n:n%2==0,l))





