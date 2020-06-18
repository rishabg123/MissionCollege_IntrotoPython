# 6.9

def footToMeter(foot):
    meter = foot * 0.305
    print(meter)
def metrerTofFoot(meter):
    foot = meter/0.35
    print(foot)
print(footToMeter(eval(input("Enter an amount of feet to convert: "))))
print(metrerTofFoot(eval(input("Enter an amount of meters to convert: "))))

#6.18
from random import randint

def printMatrix(n):
    for i in range(n):
        for j in range(n):
            print(randint(0, 1), end="")
        print("")
number = input("Choose your number: ")
printMatrix(int(number))

# 6.6

def displayPattern(n):
    for num in range(n):
        for i in range(num):
            print(num, end=" ")
        print(" ")
print(displayPattern(eval(input("Enter a number: "))))

# 6.10

def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            return False
        divisor += 1
    return True

for i in range(10000):
    if isPrime(i) == True:
        print(i)

# 6.39

import turtle
import tkinter

turtle = turtle.Turtle()

count = 1
while count <= 5:
    turtle.forward(300)
    turtle.right(144)
    count = count + 1
tkinter.mainloop()