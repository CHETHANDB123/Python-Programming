#function Aliasing
'''
def eat(food):
    print("eating process")
consume=eat #functionaliasing
consume('a')
eat('d')
'''
#Higher Order Function
def python_exam():  #call back function
    print("python exam conducted")
def java_exam():    #call back function
    print("java exam conducted")
def start_exam(subject):  #higher order function
    subject()
    #subject()
start_exam(python_exam)
start_exam(java_exam)


#passing Location
def python_exam(location):  #call back function
    print("python exam conducted",location)
def java_exam(location):    #call back function
    print("java exam conducted",location)
def start_exam(subject):  #higher order function
    subject('BTM')
    #subject()
start_exam(python_exam)
start_exam(java_exam)

