
import random

#4.9

print("Enter the weight for package 1")
weight1 = float(input())
print("Enter the price for package 1")
price1 = float(input())
print("Enter the weight for package 2")
weight2 = float(input())
print("Enter the price for package 2")
price2 = float(input())

if (weight1/price1) < weight2/price2:
    print("Package 2 is a better price")
else:
    print("Package 1 is a better price")


print("Enter the length of side 1")
side1 = int(input())
print("Enter the length of side 2")
side2 = int(input())
print("Enter the length of side 3")
side3 = int(input())

if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    print("The permimeter is", side1 + side2 + side3)
else:
    print("Not a valid triangle")


#4.8

print("Enter number 1")
num1 = int(input())
print("Enter number 2")
num2 = int(input())
print("Enter number 3")
num3 = int(input())
array = []
array.append(num1)
array.append(num2)
array.append(num3)
array.sort()
for i in array:
    print(i)


#4.10

num1 = random.randint(0, 100)
num2 = random.randint(0,100)

print("The problem is", num1, "*", num2)
print("Enter the answer")
answer = int(input())
if answer == (num1 * num2):
    print("That is correct! The answer is")
else:
    print("That is wrong. The answer is", num1*num2)


#4.13

import sys
status = eval(input("(0-single filer, 1-married jointly" + "2-married seperately, 3-head of household, " + "Enter the Filing Status: "))
income = eval(input("Enter the taxable income: "))
tax = 0
if status == 0:
    a,b,c,d,e = 8350, 33950, 82250, 171550, 372950
elif status == 1:
    a, b, c, d, e = 16700, 67900, 137050, 208850, 372950
elif status == 2:
    a, b, c, d, e = 8350, 33950, 68525, 104425, 186475
elif status == 3:
    a, b, c, d, e = 11950, 45500, 117450, 190200, 372950
else:
    print("Error: invalid status")
    sys.exit()

if income <= a:
    tax = income * 0.10
elif income <=b:
    tax = a * 0.10 + (income - a) * 0.15
elif income <=c:
    tax = a * 0.10 + (b-a) * 0.15 + (income - b) * 0.25
elif income <=d:
    tax = a * 0.10 + (b - a) * 0.15 + (income - b) * 0.25 + (income - c) * 0.28
elif income <= e:
    tax = a * 0.10 + (b - a) * 0.15 + (income - b) * 0.25 + (income - c) * 0.28 + (income - d)
else:
    tax = a * 0.10 + (b - a) * 0.15 + (income - b) * 0.25 + (income - c) * 0.28 + (e-d)
print("tax is", format(tax, ".2f"))