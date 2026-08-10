#List
list1=[1,2,3,4]
print(list1)

a=[]  #Default_value
print(a)
print(type(a))

b=list() #Second way of creating a empty list
print(b)
print(type(b))

print(len(b))

#list with elements
c=[10,20,30,4.1,False,2-8j,10] # List allows duplicate
print(c)
d=[1,2,3,4,5]
print(d[0])  # Acess index
print(d[-1])  # - index
print(len(d))
#modify list
d[0]=True
print(d)


##SET

x=set()
print(x)
print(type(x))
print(len(x))



fs={10,3.3,4,True,2-100j}
print(fs)
fs.add(99) #add
print(fs)

ref1=fs.pop() #pop
print(fs)

fs.remove(99) #remove
print(fs)

fs.discard(3.4) #discard
print(fs)

ps={2,3,4,9}  #update
fs.update(ps)
print(fs)

s1={1,2,3}
s2={1,2,3,4}
b1=s1.issubset(s2) #checks if all of this set present in another set
print(b1)

b2=s2.issuperset(s1) # checks if set has all elements of another set
print(b2)

un=s1.union(s2) #returns a new set having unique elements from both sets
print(un)

ins=s1.intersection(s2) #returns a new set having common elements from both sets
print(ins)

diff=s2.difference(s1)  # return a new set having only elements of s1 but one not present in s2
print(diff)

b3=s1.isdisjoint(s2)  # checks if there no common elements b/w 2 sets
print(b3)

s1={1,2,3}
s2={4,5,6}
d=s1.isdisjoint(s2)  
print(d)

a1={10,20,40,70}
a2={10,30,60}     # return uncommon elements of both set
d=a1.symmetric_difference(a2)  #Symmetric_difference
print(d)


ns={1,2,3,4}
ns1=ns.clear() #clear all elements in the set
print(ns1)




