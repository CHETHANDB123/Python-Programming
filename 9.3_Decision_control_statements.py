#DCS
'''
#if
x=(input("enter a name" )
if x=='Gunda':
    print("true")

print("end")
'''
'''
#if-else
y=int(input("Enter a nmber"))
if y>0:
    print("+ive number")
else:
    print("-ive number")

cr=input("Enter a chracter:")
if "a" in cr:
    print("charcter found")
else:
    print("charcter not found")

#if-elif-else
m=int(input("enter the marks")) #eval()
if m>=90 and m<=100:
    print("Topper")
elif 80>m>89:
    print("Distniction")
elif m>60 and m<=80:
    print("1st class")
elif m>40 and m<=60:
    print("2nd class")
elif m==35 and m<=40:
    print("pass")
elif m>0 and m<35:
    print("Future of India")
else:
    print("Invalid")

#Match case

w=int(input("Enter the week day"))
match w:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thrusday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7 | 0:
        print("Sunday")
    case _:
        print("Invalid")
print("==================")


#nested-if
email=input("Enter the email")
if email=="chethna@gmail.com":
    password=int(input("Enter the password"))
    if password==1234:
        print("login Successful")
    else:
        print("Incorrect Passwrd")
else:
    print("Invalid email")

# Conditional Exp
n=12
if n>0:
    print("+ive")
else:
    print("-ive")

#TrueExp if condition else falseExp
res="+ive" if n>0 else "-ive"
print(res)

a=5
age="Eligible vote" if a>18 else "not eligible"
print(age)
'''
num=4
resl=num+10 if num>0 else num-5
print(resl)



















