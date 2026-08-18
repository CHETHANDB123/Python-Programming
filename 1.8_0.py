#packing
''''
p=1,2,3,4
print(p)
print(type(p))

#unpacking
l=[1,2,3,4]
a,b,c,d=l
print(a,b,c,d)

l1=[1,2,3,4,5,6,7,8,9,11]
*a,b,c=l1
print(a,b,c)
a,*b,c=l1
print(a,b,c)
a,b,*c=l1
print(a,b,c)

a,b,*c='chethan'
print(c)
#Argument
# 1) positional Arg
def movie(movie_name,theater,cost):
    print(movie_name)
    print(theater)
    print(cost)
movie("spier",'urvashi',200)

#2) keyword Arg
def movie(movie_name,theater,cost):
    print(movie_name)
    print(theater)
    print(cost)
movie(cost=200,movie_name='spider',theater='urvashi')

#3) Variable length Arg
#var pos Arg
#packing
def collect(*king):
    print(king)
collect(1,2,3,4,55,66,76,0)

#unpacking
def collect1(a,d,c):
    print(a)
    print(d)
    print(c)
l=[10,20,30] #list - Tuple
collect1(*l)

def combine(*arg):
    print(arg)
l=[1,2,3]
combine(*l)
##
##def combine(*arg):
##    print(arg)
##l=[1:10,2:20,3:30]
##combine(*l)

def gather(**kr): #packing
    print(kr)
gather(name='chethan',age=22,marks=00) #Tuple-dict
    

def disperse(name,age,marks): #unpacking
    print(name) 
    print(age)
    print(marks)
d={'name':'chethan','age':22,'marks':222}
disperse(**d)

def together(**ka):  #**ka packing
    print(ka)    
d={'name':'chethan','age':22,'marks':222}
together(**d)       #**d unpacking

'''
#4) Degault Argument
def organise_event(drinks='water',start=10,snacks='somasa'):
    print(drinks)
    print(start)
    print(snacks)
organise_event()
organise_event('aaa')
organise_event('bbb',22,'www')
organise_event(snacks='gooday',drinks='sprite',start=200)












