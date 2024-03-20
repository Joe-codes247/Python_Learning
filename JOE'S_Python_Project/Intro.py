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



"""
#Nationality check program
visitors = int(input("Enter the number of visitors:"))
ugno = 0
kenyano = 0
counter = 1
while counter <= visitors:
  nationality = input("Enter the nationality:")
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
"""


#for loop in python
colours = ["blue", "yellow", "red"]
for x in colours:
  print(x)

#nested loops using range
adj = ["Red", "Green", "orange"]
fruits = ["apple", "banana", "orange"]
for x in adj:
  for y in fruits:
    for z in range(3):
      print(x,y)

#converting tuples to list
fruits = ("apple", "banana", "orange")
print(fruits)
myfruits = list(fruits)
myfruits[1] = "mangoes"
myfruits.append("pineapple")
fruits = tuple(myfruits)
print(fruits)

#python dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

#creating a function
def addition(x,y):
  return x + y

#calling a function
print("The sum of 5 and 9 is:",addition(5,9))

#function question on list finding the largest number
def fluid_largest_number(numbers):
     max_number = float('-inf')
     for num in numbers:
       if num > max_number:
           max_number = num

     return max_number

my_list = [1,2,3,400,5]
largest_number = fluid_largest_number(my_list)
print("Largest number is:",largest_number)

#Repeated element list
my_list = ["apple", "banana", "cherry", "banana", "banana", "apple"]
repeated_elements = []

for item in my_list:
  if my_list.count(item) > 1:
      repeated_elements.append(item)
print(repeated_elements)


















