#
'''
def decorator(fun):  #outer fun
    def wrapper():  #inner fun
        print("take a gift paper")
        fun()  #gift( )
        print("place a label on the gift")
    return wrapper
def gift(): #orignal fun to be decorated
    print("smiling Buddha is selecting as gift")
gift=decorator(gift)
gift()  #Wrapper calling

def decotator(cake):    #step 2
    def wrapper(flavour,name):      #step 3
        print("Take cake mould")
        cake(flavour,name)
        print("place a honey, Icing on the cake")
    return wrapper     #step 4
def bake(flavour,name):         #step 1
    print(f"{flavour} is selected flavour,cake from {name}")
bake=decotator(bake)    #step 5
bake("Honey","iyengar")
'''
def decotator(cake):    #step 2
    def wrapper(*args,**kwargs):      #step 3
        print("Take cake mould")
        cake(*args,**kwargs)
        print("place a honey, Icing on the cake")
    return wrapper     #step 4
@decotator
def bake(*args,**kwargs):         #step 1
    print(" honey cake is selected flavour,cake ",args,kwargs)
#bake=decotator(bake)    #step 5
bake("maida","egg","sugar",flavour="velvet",cream="amul",cost=300) #wrapper

##
##def pizza_topping(*args,**kwargs):
##    print("selcetd a pizza",args,kwargs)
##
##pizza_topping=decotator(pizza_tooping)



