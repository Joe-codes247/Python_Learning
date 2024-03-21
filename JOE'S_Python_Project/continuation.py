#updating tuples
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#alternative 2
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("mango")
thistuple = tuple(y)

print(thistuple)

#alternative 3
thistuple = ("apple", "banana", "cherry")
y = ("orange", "melon", "pawpaw")
thistuple += y

print(thistuple)

#Removing items from dictonary
thisdict =	{
  "brand": "Devel",
  "model": "Super car",
  "year": 1964,
  "Speed": "450km/h",
}
thisdict.pop("model")
print(thisdict)

#Checking the existence of a value in a dictionary
thisdict = {
  "brand": "Devel",
  "model": "Super car",
  "year": 1964,
  "Speed": "450km/h",
}
if "brand" in thisdict:
    print("Available")

#converting lists to dict
list1 = ["model", "year", "brand"]
list2 = ["Harrier", "2020", "Toyota"]
print("My list 1", list1)
print("My list 2", list2)
mydict = dict(zip(list1,list2))
print("My dict", mydict)




