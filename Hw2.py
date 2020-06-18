# 2.4
import math

print("Enter an amount of pounds to convert: ")
pounds = float(input())
print(pounds * 0.454)


#2.13
print('Enter a number')
number = int(input())
numberArray = []
while number > 0:
    numberArray.append(int(number % 10))
    number = int(number / 10)
numberArray.reverse()
for i in numberArray:
    print(i)


# 2.1

print("Enter a celcius degree")
degree = float(input())
farenheit = (9/5) * degree + 32
print(farenheit)

# 2.2

print("Enter a radius")
radius = float(input())
print("Enter a length")
length = float(input())
area = radius * radius * math.pi
volume = area * length
print("The area is:",area)
print("The volume is",volume)

# 2.10

print("Enter a meters per second")
metersPerSecond = float(input())
print("Enter an acceleration")
acceleration = float(input())
print("The minimum length of the runway needs to be:", math.pow(metersPerSecond,2) / (2*acceleration))