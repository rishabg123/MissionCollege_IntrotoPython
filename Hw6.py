# 6.9

def footToMeter(foot):
    meter = foot * 0.305
    return meter
def meterToFoot(meter):
    foot = meter/0.305
    return foot

print(footToMeter(eval(input("Enter an amount of feet to convert: "))))
print(meterToFoot(eval(input("Enter an amount of meters to convert: "))))

#6.18
from random import randint

def printMatrix(n):
    for i in range(n):
        for j in range(n):
            print(randint(0, 1), end="    ")
        print("")
        print("")
number = input("Choose your number: ")
printMatrix(int(number))

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

print()
print()

# 6.10
def isPrime(n):
   if n <= 1:
       return False


   for i in range(2, n):
       if n % i == 0:
           return False

   return True

def printPrime(n):
   printedPrimecount = 0
   for i in range(2, n + 1):
       if isPrime(i):
           print(i, end=' ')
           printedPrimecount += 1
           if printedPrimecount % 20 == 0:
               print()


if __name__ == "__main__":
   n = 10000
   printPrime(n)
   print()
   print()
   print("There are 1229 prime numbers")


# 6.39

import turtle
def drawStar(x1, x2, y1, y2, x3, y3, x4, y4, x5, y5, x6, y6):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)
    turtle.goto(x3, y3)
    turtle.goto(x4, y4)
    turtle.goto(x5, y5)
    turtle.goto(x6, y6)

turtle.showturtle()
drawStar(-111, -68, -50, 122.65, -11.8, -68, -150, 50, 30, 50, -111, -50)
turtle.done()