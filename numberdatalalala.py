""" x = 3
y = float(3)
print(x,y) """

""" values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i)

print(values[0])
print(values[6]) """

""" "test"
["t","e","s","t"]

x = "this is a thing"
y = x.split( )
z = y[0]
print(y)
print(z) """

""" day_of_week = input("what day is it?")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect") """ 
""" 
x = "test"
print(f"hello {x}") """
""" 
temp = 75
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """

""" bill = float(input("bill?"))
tip = float(input("how much tip?"))
total = bill+tip
if bill > 0:
    print(tip)
if tip >= 0:
    print(total) """

bill = int(input("your bill..hmmm?"))
service = input("great, good, okay, bad, horrid")
def getTip(bill, service):
    if service == "great":
        print(bill*0.25)
    if service == "good":
        print(bill*0.2)
    if service == "okay":
        print(bill*0.15)
    if service == "bad":
        print(bill*0.1)
    if service == "horrid":
        print(0)




""" number = int(input("give me number"))

if number >= 21:
    print("can vote and gamble")
elif(number >= 18):
    print("Can vote but not gamble")
else:
    print("have a juicebox kid")

temp = 55
if (temp > 40 and temp < 60):
    print("lightjacket need")
elif (temp < 20 or temp > 90):
    print("extreme") """

""" age = int(input("give age"))
def discount(isMember, age, isResident):
    if (isMember or isResident):
        print("discount applies")
    if age >=65:
        print("discount applies")
    if age <=12:
        print("discount applies")
    else:
        print("discount does not apply") #uhohs??? """