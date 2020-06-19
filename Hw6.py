# # 6.9
#
# def footToMeter(foot):
#     meter = foot * 0.305
#     return meter
# def metrerTofFoot(meter):
#     foot = meter/0.35
#     return foot
#
# print(footToMeter(eval(input("Enter an amount of feet to convert: "))))
# print(metrerTofFoot(eval(input("Enter an amount of meters to convert: "))))
#
# #6.18
# from random import randint
#
# def printMatrix(n):
#     for i in range(n):
#         for j in range(n):
#             print(randint(0, 1), end="")
#         print("")
# number = input("Choose your number: ")
# printMatrix(int(number))

# 6.6
n = int(input("Enter a value for n: "))
def displayPattern(n):
    for i in range(1, n + 1):
        for j in range(n, 0, -1):
            if j > i:
                print("  ", end='')
            else:
                print(j, end=" ")

        print("")


displayPattern(n)

# 6.10

# def isPrime(number):
#     divisor = 2
#     while divisor <= number / 2:
#         if number % divisor == 0:
#             return False
#         divisor += 1
#     return True
#
# for i in range(10000):
#     if isPrime(i) == True:
#         print(i)
#
# # 6.39

import turtle
import tkinter
def draw_star():
    print("Input an amount of sides you want for the star")
    sides = int(input())
    angle = 120


    for side in range(sides):
        turtle.forward(100)
        turtle.right(angle)
        turtle.forward(100)
        turtle.right(360/sides - angle)


draw_star()

tkinter.mainloop()

