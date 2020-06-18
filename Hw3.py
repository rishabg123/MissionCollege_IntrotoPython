import math
#3.4

print("Enter a side of a pentagon: ")
length = float(input())
numerator = 5 * math.pow(length,2)
denom = 4 * math.tan((math.pi) / 5)
print("The area of the pentagon is", numerator/denom)

#3.6

print("Enter a number for ASCII")
val = int(input())
print("The ASCII is", chr(val))

#3.5

print("Enter the number of sides: ")
number = float(input())
print("Enter the length of each side")
length = float(input())
numer = number * (length * length)
denominator = 4 * (math.tan(math.pi / number))
print("The area of the polygon is", numer/denominator)

#3.10

print("The Greek symbols are: ", "\u03b1 \u03b2 \u03b3 \u03b4 \u03b5 \u03b6 \u03b7 \u03b8")

#3.11

print("Enter a number: ")
number = int(input())
numberArray = []
while number > 0:
    numberArray.append(int(number % 10))
    number = int(number / 10)
for i in numberArray:
    print(i, end='')


