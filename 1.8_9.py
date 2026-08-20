'''
a=100    #GV
def outer():
    b=200 #b is LV of outer fun / ENCLOSING VARIABLE
    print("accessing GV inside the outer fun",a)
    print(b)
    def inner():
        print("accessing GV inside the inner fun",a)
        print(b)
        pass
    inner()                     
outer()

#Enclosing var
def outer():
    a=100   #enclosing var
    a+=50
    print(a)
    def inner():
        print("inner function body")
    inner()
outer()
##
def outer():
    a=100   #enclosing var
    def inner():
        nonlocal a
        a+=20
        print(a)
        print("inner function body")
    inner()
outer()
'''
def counter():
    a=0
    def increment():
        nonlocal a
        a+=1
        print(a)
    increment()
    increment()  
    increment()
counter()















