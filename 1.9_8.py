#creating genertor function
#LAZY Evaluator
'''
def fun():   #generator fun
    print("hi")
    yield 10
    yield 20
gen_obj=fun()  #generator object is created when geneartor fun call
print(gen_obj)
print(next(gen_obj))
print(next(gen_obj))
#print(next(gen_obj))  StopIteration
'''
##
def fun():    #1)generator fun helps in creating custom sequence
    value=1
    yield value**1
    value+=2
    yield value**2
    value+=3
    yield value**3
    value+=4
    yield value**4
gen_obj=fun()

print(list(gen_obj)) #1.1)using Explicit gen obj exhauseted

for i in gen_obj:  #2)using for loop generator object can exhausted
    print(i)
'''
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
'''

