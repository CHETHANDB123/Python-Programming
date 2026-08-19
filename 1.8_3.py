#Types of variables
#Global Var
'''
a=100 #GV
b=20
def dispaly():
    global a,b
    print(a,"accessing G V inside fun")
    a=a+50  # modifying G V inside fun
    print(a)
    b=b+30
    print(b)
    
dispaly()
print(a,"accessing G V outside fun")
a=a+100 # modifying G V outside fun
print(a)  # modifying G V outside fun
'''
#Local Var
def show(a):
    #a=100 LV
    a+=50
    print(a,"modify of LV")
    print(a,"LV can be accseeed inside function")
show(500)
#print(a) cannot be accessed outside fun
