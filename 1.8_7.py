#nested_function
def outer():                          #outer FD
    print("outer function body")    
    def inner():                    #inner FD
        print("inner function body")
    inner()                     #inner FC
outer()                         #outer FC
print("-----")
outer()
