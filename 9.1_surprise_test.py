'''
#1
players=["messi","ronaldo","chettri"]
country=["Argentina","portugal","india"]
d=dict(zip(players,country))
x=d.pop("chettri")
print(d)
print(x)

#3
s=input("Enter the name")
w=s.upper()
b=w[-5:-8:-1]
c=w[-1:-4:-1]
d=c+b
print(d)

#3
s="encychopedia"
print(s)
w=s.upper()
print(w)
##a=w[-1:-4:-1]
##b=w[-10:-13:-1]
a=w[:3]
b=w[-1:-4:-1]
cs=a+b
s=cs[::-1]
#c=a+b
print(s)

#2
item_name=input("enter the name")
quantity=int(input("enter quantiy"))
price=int(input("enter cost"))
amount=quantity*price*0.1
print(f"Itemname:{item_name},Quantity:{quantity},price:{amount}")
           
#5
s="   10 20 30   "
w=s.strip()
print(w)
s1=w.split()
print(s1)
print(int(s1[0])+int(s1[-1]))
          
'''
#4
area=input("Enter area:")
perimeter=input("Enter perimeter:")
a=f"Area of circle having radius r is {area}"
b=f"perimeter of circle having r is {perimeter}"
print(a)
print(b)
