print("Hello, World!")

if 7>6:
	print("Seven is greater!")

if 7>20:
	print("Seven is greater!")
else:
	print("Twenty is greater!")

#This prints hello world
print("Both of both Worlds!")


print("Rock the World")#This is a comment

"""
print("Hello, World!")

"""

x = 5
y = "John"
print(x)
print(y)

p = open("demofile.txt", "r")
print(p.read())

q = open("demofile.txt", "r")
print(q.readline())


f = open("demofile.txt", "r")
for x in f:
  print(x)


u= open("demofile.txt", "r")
print(u.readline())
u.close()

e = open("demofile2.txt", "a")
e.write("Now the file has more content!")
e.close()

#open and read the file after the appending:
e = open("demofile2.txt", "r")
print(e.read())

g = open("demofile2.txt", "w")
g.write("Woops! I have deleted the content!")
g.close()

#open and read the file after the appending:
g = open("demofile2.txt", "r")
print(g.read())


#print(open("myfile.txt", "x"))
"""
import os
k = os.remove("demofile.txt")
print(k)
"""

price = 49
txt = "The price is {} dollars"
print(txt.format(price))

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 9
itemno = 5986
price = 15
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "1967 Impala", model = "Chevrolet"))

a = " Priyanka Mahakud "
print(a.strip())

a = " Priyanka Mahakud "
print(a.lower())

a = " Priyanka Mahakud "
print(a.upper())

a = "Priyanka Mahakud"
print(a.replace("h", "y"))

a = "Priyanka , Mahakud!"
print(a.split(","))

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
print(len(thislist))

txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)

thatlist = ["apple", "banana", "cherry"]
thatlist.append("orange")
print(thatlist)

fruitlist = ["apple", "banana", "cherry"]
fruitlist.remove("banana")
print(fruitlist)

justlist = ["dhoni", "watson", "curran"]
justlist.pop()
print(justlist)

ipllist = ["merlin", "arthur", "gene"]
del ipllist

seclist = list(("sin", "cos", "tan"))
print(seclist)

def my_function():
  print("My first my function")
my_function()

def let_function(fname):
  print(fname + " Amazing")

let_function("Emmanuel")
let_function("Rocking")
let_function("Lenus")

i = 1
while i < 6:
  print(i)
  i += 1


j = 1
while j < 9:
  print(j)
  if j == 6:
    break
  j=j+1

k = 1
while k < 8:
  print(k)
  k = k+ 1
else:
  print("k is no longer less than 8")

#local scope
def myfunc():
  x = 300
  print(x)

myfunc()

def fun():
  x = 13456
  def sun():
    print(x)
  sun()

fun()

def greeting(name):
  print("Hello, " + name)


x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

x = abs(-7.25)
print(x)

x = pow(4, 3)
print(x)

import math
x = math.sqrt(121)
print(x)