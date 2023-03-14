# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 21:27:13 2023

@author: TUGCE
"""

#The first value is added when the variable is written.

x = 5
name = "Tugce"
print(x)
print(name)

#The type of the variable can be easily changed with new assignments.

x2 = 10
print(x2)
x2 = "Umut"
print(x2)

#Local variables are defined only in the code block they are defined in, while global variables are defined throughout our code.

x3 = "Programming"
def myfunc():
  x3 = "Programlama"
  print("Python " + x3)

myfunc()
print("Python " + x3)

#Detecting Data Type

x4 = 234
print(type(x4))

#Variable's Data Type

x5 = str("Hello World")
x6 = int(25)
x7 = float(25.5)
x8 = list(("purple", "blue", "yellow"))
x9 = True

#Converting Numeric Types to Each Other

x10 = 1    # int
x11 = 2.8  # float

#convert int to float:
a = float(x10)
print(a)
#convert float to int:
b = int(x11)
print(b)

# + Operator
x12 = 10
x13 = 20
result = x12 + x13
print(result)

# - Operator
x14 = 50.5
x15 = 12.7
result2 = x14 - x15
print(result2)

# * Operator
x16 = 7
x17 = 13.1
result3 = x16 * x17
print(result3)

# / Operator
x18 = 5
x19 = 2
result4 = x18 / x19
print(result4)

# % Operator
x20 = 2023
x21 = 2
result5 = x20 / x21
print(result5)

#AND Operator
x22 = 18
x23 = "purple"
result6 = (x22>=18) and (x23=="purple")
print(result6)

#OR Operator
x24 = 18
x25 = "purple"
result7 = (x24>=18) or (x25=="yellow")
print(result7)

#NOT Operator
x26 = 5
result8 = not(x26 > 3 and x26 < 10)
print(result8)

#Logical Operator

x27 = float(input('Number: '))
result9 = (x27 > 0) and (x27<=100)
print(f'Is the number between 0-100?: {result9}')

email = 'email@email.com'
password = 'abc123'
enteredEmail = input('email: ')
enteredPassword = input('password: ')
result10 = (enteredEmail == email) and (enteredPassword == password)
print(f'Is the application successful?: {result10}')


# If / Elif / Else 

num = float(input("enter number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    elif num == 1:
        print("One")
    else:
        print("Positive Number")
else:
    print("Negative Number")


# For

numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
sumValue = 0 

for number in numbers: 
  sumValue = sumValue + number

print("Total value: ", sumValue)

# for i in <range>:
for i in range(0,3):
    print(i)

# while

counter = 0
while counter < 3:
    print("in the loop")
    counter = counter + 1
else:
    print("outside the loop")






















