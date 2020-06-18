from turtle import *

# 1.9
print("Area of a rectangle:", 4.5 * 7.9)


# 1.15
turtle = Turtle()

turtle.goto(0,0)
for i in range(3):
    turtle.forward(100)
    turtle.right(120)

turtle.right(60)
turtle.penup()
turtle.forward(100)
turtle.pendown()

for i in range(3):
    turtle.forward(100)
    turtle.right(120)

#1.3

print("FFFFFFF   U     U   NN     NN")
print("FF        U     U   NNN    NN")
print("FFFFFFF   U     U   NN N   NN")
print("FF         U   U    NN  N  NN")
print("FF          UUU     NN    NNN")

print("")


#1.10
print("Average Speed in mph:",(14/1.6)/0.7583333)


# 1.11
time = 3600 * 24 * 365
born = time // 7
death = time // 13
immigrant = time // 45

current_population = 312032486
population = born + immigrant - death

for i in range(5):
    current_population = current_population + population
print("Population after 5 years:",current_population)






