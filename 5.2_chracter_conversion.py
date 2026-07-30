#converting a chrater numeric value it is part of single valued type casting
#python internally represents ervery character by unique code , it is a unique number which is assined that characeter , 2 character invalid fun name is ORD
#ord('character')
# it is predefined fun that return the unique code(int) of the given char

#A-65
#Z-90
#a-97
# -32
#0-48

c1=chr(65) #Converts int to character
print(c1)
c2=chr(22)
print(c2)
c3=chr(1)
print(c3)
c4=chr(90)
print(c4)
print(chr(23566))
print(chr(128512))
print(chr(999999))
print("==========")

print(ord("A")) #ord=convert character to number
print(ord("0")) #pass only str of length 1
print(ord("a"))
print(ord("😀"))#128512

#chr(intergernumber)
#It reurn the corresponding char associate for the number

'''
number=int(input("enter int munber"))
print(number+10)
height=float(input("enter heiht"))
print(height+3)

h=(input("are u male"))
print(bool(h))
'''

r=eval("1*7+2")
print(type(r))
print(r)
print(type(r))

print("========")
