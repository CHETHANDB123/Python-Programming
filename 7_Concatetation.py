#cont

country_name="spain"
result="won"
sport="footbal"
opponent="Argentina"

f=country_name+" "+result+" "+"the "+sport+" "+"Game "+"against "+opponent
print(f)
"""
p_name=input("enter player name") 
goal=int(input("enter the goal scored by the player"))
height=float(input("enter the player height"))
country=eval(input("is he from Argentina"))

#m=p_name+" "+"who is a"+" "+str(country)+" "+"Argentina player has scored "+str(goal)+"goals and height is"+str(height)
#format string
m=f"{p_name} who is a {country} Argentina player has scored {goal} goals And height is {height}"
print(m)
"""


name="chethan"
speed=66
weight=33.44
#print(f"{name} weights {weight} kg and at {speed} mph")
print("{} weights {}kg and at {} mph".format(name,weight,speed))
