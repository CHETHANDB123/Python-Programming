#function
'''
def wish(): #FD
    print('good bye') #FB
wish() #FC

#1)without parameter & without return
#def a func , which name  as dispaly
def display():
    print("1 Dosa")
    print("2 idle")
    print("3 vada")
display()

#2)without parameter & with return
def party():
    print("happy birthday")
    return "honeycake"
print(party())

def wether_status():
    print("fetching wether datails")
    return "cloudy"
print(wether_status())


#3)with parameter & without return
def register(name,phoneNo):
    print("user register successfully")
register('chethan',11111111)

def reg(name,phone):
    #print(name,"register successfully",phone)
    print(f"{name} register successfully {phone}")
reg('chethan',2222222)

def otp(phone):
    print("OTP sent successfully to this",phone)
otp(111111)
'''

#4)with parameter & with return
def add(o,t):
    return o+t
print(add(1,2))

def sub(n1,n2):
    return n1-n2
print(sub(3,4))

def muti(n1,n2):
    return n1*n2
print(muti(3,4))

def div(n1,n2):
    return n1//n2
print(div(4,2))




























    
