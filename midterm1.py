# Problem 1

# print("Enter the balance")
# balance = float(input())
# print("Enter the percentage rate")
# rate = float(input()) / 100
#
# print("The interest rate in the next month is", balance * rate * 1/12, "dollars")

# Problem 2
#
# import turtle
# import tkinter
# import math
#
# style = ('Courier', 10, 'italic')
# style2 = ('Courier', 30, 'italic')
#
# print("Enter x1")
# x1 = float(input())
# print("Enter y1")
# y1 = float(input())
# print("Enter x2")
# x2 = float(input())
# print("Enter y2")
# y2 = float(input())
# print("Enter x3")
# x3 = float(input())
# print("Enter y3")
# y3 = float(input())
#
# turtle = turtle.Turtle()
# turtle.penup()
# turtle.goto(0,0)
# turtle.pendown()
# turtle.goto(x1,y1)
# turtle.write("%d, %d"%(x1, y1), font=style, align='center')
# turtle.right(60)
# turtle.goto(x2,y2)
# turtle.write("%d, %d"%(x2, y2), font=style, align='center')
# turtle.right(60)
# turtle.goto(x3,y3)
# turtle.write("%d, %d"%(x3, y3), font=style, align='center')
# turtle.right(60)
# turtle.goto(x1,y1)
# turtle.hideturtle()
#
# base = math.sqrt(math.pow(2, x2-x1) + math.pow(2, y2-y1))
# midpointx = (x1 + x2)/2
# midpointy = (y1 + y2)/2
# base = math.sqrt((math.pow(x2-x1, 2)) + math.pow(y2-y1, 2))
# height = math.sqrt((math.pow(x3-midpointx, 2)) + math.pow(y3-midpointy, 2))
# area = (1/2 * base) * height
# turtle.penup()
# turtle.goto(0, -100)
# turtle.write("%f"%(area), font=style2, align='center')
#
# tkinter.mainloop()


# Problem 3

pointx = int(input("Enter a coordinate for x: "))
pointy = int(input("Enter a coordinate for y: "))
rectanglex = 10
rectangley = 5
if pointx <= rectanglex and pointy <= rectangley and pointx >= 0 and pointy >= 0:
   print("Inside the Rectangle")
else:
   print("Outside the Rectangle")

# Problem 4

print("Enter 0 when you finish entering your integers")
prompt = int(input("Enter an integer: "))
pos = 0
neg = 0
total = 0
inputCount = 0
while prompt != 0:
   total += prompt
   inputCount += 1

   if prompt < 0:
       neg += 1
   elif prompt > 0:
       pos += 1

   prompt = int(input("Enter an integer: "))

if pos == 1:
   print("There is 1 positive integer")
else:
   print("There are", pos, "positive integers")

if neg == 1:
   print("There is 1 negative integer")
else:
   print("There are", neg, "negative integers")

print("The sum of the integers is", total)
print("The average of the integers is", total/inputCount)