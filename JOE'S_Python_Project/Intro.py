x,y,z = "PS2", "PS3", "PS4"
print(x)
print(y)
print(z)

elements = ["fire", "air", "water", "earth"]
w,x,y,z = elements
print(w)
print(x)
print(y)
print(z)

x = "awesome"
def myfunc():
  print("Gaming is " + x)

myfunc()

#operators
x=4
x+=4
x=x+3
print("My answer is:",x)

y=4
z=5
print(y==z)

#the if...elif statemnt
age=5
if age>=18:
  print('You are an adult')
elif age<18:
  print("child")

#if...elif...else statement
a = 10
b = 33
if a > b:
  print("a is greater than b")
elif a == b:
  print("a is equal to b")
else:
  print("a is less than b")


country="Kenya"
if country=="Kenya":
  print("selected")
elif country=="Tanzania":
  print("selected too")
else:
  print("not selected")


#using the and statement
president_age = 10
nationality = "Kenya"

if president_age >=18 and nationality=="Kenya":
  print("You are a president")
else:
  print("You are not a president")


#checking the not equal to operator
if(country!="Uganda"):
  print("You have never been to Kampala")

#checking the or statement
nationality = "Kenya"

if nationality=="Kenya" or nationality=="Uganda" or nationality=="Tanzania":
  print("You qualify for CECAFA")   #Executes if one of the conditions is met
else:
  print("You dont qualify")

#checking even and odd numbers
y = 8
if y%2==0:
  print("Even")
else:
  print("odd")

#casting integer to string
first_name = "Joe"
last_name = 4
full_name = first_name+" "+str(last_name)
print(full_name)

#float to string
bucket = 20.0
books = "50.0"
total = bucket+float(books)
result = "the total is:"+str(total)+" Kenya shillings"
print(result)


#the while loop
z = 1
while z < 12:
  print(z)
  z += 1

#Nationality check program
visitors = int(input("enter the number of visitors"))
ugno = 0
kenyano = 0
counter = 1
while counter <= visitors:
  nationality = input("enter the nationality:")
  if nationality == "Kenyan":
      kenyano += 1
      print("Allowed")
      counter += 1
  else:
    ugno += 1
    print("Not allowed")
    counter += 1

print("The number of visitors is:",visitors)
print("The number of Kenyans is:",kenyano)
print("The number of ugandans is:",ugno)








