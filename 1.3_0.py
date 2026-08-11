##Dictionary
dic={}
print(dic)
print(type(dic))

ed=dict()
print(ed)
print(type(ed))
print(len(ed))


fd={10:1903,2.2:9.4,3:1903}
print(fd)
print(type(fd)) #type fun
print(len(fd))

#access a value
#print(ref[key])
print(fd[2.2])

#update the value based on key
fd[10]=1000
print(fd)

fd[30]=300 # if u give new key & value , a new item is created
print(fd)

# get (key)-> return the corresponding value for key
val=fd.get(2.2)
print(val)

#set default(key,value)
fd.setdefault(11,222)
print(fd)

#pop(key)
fd.pop(11) #it removes the 
print(fd)

#.keys()=returns a view object that dispaly a list of all keys in dictionary
print(fd.keys())
'''
view object = dyanmic read only object that shows the dict keys,values,items without coying them
'''
#view clear
print(fd.clear())
#We can add only immutale as keys in dictionary


####String

name='chethan123'
print(name)
print(type(name))

n1="chethan's jksjd"
print(n1)

nick="virat khloi"
print(len(nick))
print(nick[1]) #postive index
print(nick[-2]) #negative index

#nick[0]='w' # immutable


#Methods
#.capitalize()
sub="python is programming language"
cap_sub=sub.capitalize()
print(cap_sub)

#.title()
title_sub=sub.title()
print(title_sub)

#.upper()
upper_sub=sub.upper()
print(upper_sub)

#.isupper()
b_isupper=sub.isupper()
print(b_isupper)

#.lower()
lo_sub=sub.lower()
print(lo_sub)

#.islower()
bl_islower=sub.islower()
print(bl_islower)

#.sawpcase
sw_swap=sub.swapcase()
print(sw_swap)

#.startswith(substring)
b3=sub.startswith('python ')
print(b3)

#.endswith(substring)
b4=sub.endswith('tage')
print(b4)

#.count()
co=sub.count(" ")
print(co)

#.index(substring)
ind_pos=sub.index('o')
print(ind_pos)

#.isalpha()->checks if str contains only alphabets
xx="iamchethan"
al=xx.isalpha() #True
print(al)

#.isdecimal()
de="1234"
is_dec=de.isdecimal() #True
print(is_dec)

#.isalnum()->alphanumeric or only alpha or only num but no special characters
is_al=xx.isalnum()
print(is_al)

#.replace('exist_substring','new_substring')
m="i love cricket"
rep=m.replace('love','hate')
print(rep)

#.lstrip()
l2='  sunday' #leading whitespaces
print(l2.lstrip())
#.rstrip()
l1='sunday   ' #trailing whitespaces
print(l1.rstrip())
#.strip()
l3='   sunday  '
print(l3.strip())

#.split()
sp="i am hero"
print(sp.split())
r=sp.split(" ") #return or store in r bcz i need in further logic
print(r)
print(len(r)) #here a logic
