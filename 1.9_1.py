'''
#Closure
def outer():  #higher order fun
    a=100   #enclosing var
    def inner(): 
        print("inner function body")
        print(a)
    return inner
inside=outer()
inside()   #Closure = inner() + a = 100
'''
def counter():
    count=0
    def increment():
        nonlocal count
        count+=1
        print(count)
        #count+=1
    return increment
inside=counter()
inside()
inside()
inside()
