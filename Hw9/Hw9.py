from turtle import Screen, Turtle

# 9.3

from tkinter import *

window = Tk()
RBrect = IntVar()
fillshape = IntVar()
crRect = IntVar()
crOval = IntVar()

c = Canvas(window, height=250, width=300)


def rectangleClick():
    global crRect, crOval;
    c.delete(crOval)
    c.delete(crRect)
    if fillshape.get():
        crRect = c.create_rectangle(120, 120, 180, 200, fill='grey')
    else:
        crRect = c.create_rectangle(120, 120, 180, 200)


def ovalClick():
    global crRect, crOval;
    c.delete(crRect)
    c.delete(crOval)
    if fillshape.get():
        crOval = c.create_oval(120, 120, 180, 200, fill='grey')
    else:
        crOval = c.create_oval(120, 120, 180, 200)


def fillit():
    global crRect, crOval;
    if fillshape.get():
        c.itemconfig(crRect, fill='grey')
        c.itemconfig(crOval, fill='grey')
    else:
        c.itemconfig(crRect, fill='')
        c.itemconfig(crOval, fill='')


c.pack()

rectangle = Radiobutton(window, text="Rectangle", variable=RBrect, value=1, command=lambda: rectangleClick())
oval = Radiobutton(window, text="Oval", variable=RBrect, value=2, command=lambda: ovalClick())
fill = Checkbutton(window, text="Fill", variable=fillshape, command=lambda: fillit())

rectangle.pack(anchor=W, side=LEFT, ipadx=10)
oval.pack(anchor=W, side=LEFT, ipadx=10)
fill.pack(anchor=W, side=LEFT, ipadx=10)
window.mainloop()

#9.4

from tkinter import *
window = Tk()
c = Canvas(window, height=500, width=500)

a = c.create_rectangle(10,190,490,490)
b = c.create_rectangle(15,195, 485, 485)
d = c.create_rectangle(20, 200, 480, 480)
e = c.create_rectangle(25, 205, 475, 475)
f = c.create_rectangle(30, 215, 470, 470)
g = c.create_rectangle(35, 220, 465, 465)
h = c.create_rectangle(40, 225, 460, 460)
i = c.create_rectangle(45, 230, 455, 455)
j = c.create_rectangle(50, 235, 450, 450)
k = c.create_rectangle(55, 240, 445, 445)
l = c.create_rectangle(60, 250, 440, 440)
m = c.create_rectangle(65, 255, 435, 435)
n = c.create_rectangle(70, 260, 430, 430)
o = c.create_rectangle(75, 265, 425, 425)
p = c.create_rectangle(80, 270, 420, 420)
q = c.create_rectangle(85, 275, 415, 415)
r = c.create_rectangle(90, 280, 410, 410)
s = c.create_rectangle(95, 285, 405, 405)
t = c.create_rectangle(100, 290, 400, 400)
u = c.create_rectangle(105, 295, 395, 395)


c.pack()

window.mainloop()

# 9.6
from _tkinter import *
from random import randint

window = Tk()
window.title("Tic-Tac-Toe")

cross = PhotoImage(file = "/Users/rishab/PycharmProjects/MissionCollege_IntrotoPython/Hw9/o.gif")
theo = PhotoImage(file = "/Users/rishab/PycharmProjects/MissionCollege_IntrotoPython/Hw9/x.gif")
for i in range(3):
    for j in range(3):
        randomNumber = randint(0,1)
        if randomNumber == 0:
            Label(window, image = cross).grid(row= i, column = j)
        else:
            Label(window,image = theo).grid(row=i, column = j)

window.mainloop()


# 9.10

import matplotlib.pyplot as plotter

# The slice names of a population distribution pie chart

pieLabels = 'Projects', 'Quizzes', 'Midterm', 'Final Exam'

# Population data

populationShare = [20, 10, 30, 40]
colors = ["red", "blue", "green", "orange"]

figureObject, axesObject = plotter.subplots()

# Draw the pie chart

axesObject.pie(populationShare,

               labels=pieLabels,

               autopct='%1.2f',

               startangle=90,
               colors=colors)

# Aspect ratio - equal means pie is a circle

axesObject.axis('equal')

plotter.show()

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('Projects', 'Quizzes', 'Midterm', 'Final Exam')
y_pos = np.arange(len(objects))
performance = [20, 10, 30, 40]

barList = plt.bar(y_pos, performance, align='center', alpha=1,color = colors)
plt.xticks(y_pos, objects)
plt.ylabel('Weighting')
plt.title('Category Weighting')



plt.show()

# 9.18

import random

turtle = Turtle()
def blink_on():
    turtle.write("WELCOME", align="center", font=("Impact", 50))
    screen.ontimer(blink_off, 200)

def blink_off():
    turtle.undo()
    screen.ontimer(blink_on, 200)

screen = Screen()

blink_on()


screen.exitonclick()

