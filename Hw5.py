#5.18

print("Enter a number")
number = int(input())
factors = []
num = number
while num != 1:
    for i in range(2, number):
        while (num % i) == 0:
            factors.append(i)
            num = num //i

print("The factors are:")
for i in factors:
    print(i)


# 5.26
from fractions import Fraction
print("")
print("The answer to the series addition is:")
numerator = 1
denominator = 3
answer = 0
while denominator != 99:
    answer = answer + (numerator/denominator)
    numerator += 2
    denominator +=2
print(Fraction(answer))

# 5.2
import time
import random

wrongCount = 0
start_time = time.time()
for i in range(10):
    num1 = random.randint(1,15)
    num2 = random.randint(1,15)
    print("The answer to", num1 ,"+" ,num2, "is: ")
    answer = int(input())
    if answer != num1 + num2:
        wrongCount += 1
end_time = time.time()
print("You got", 10 - wrongCount, "questions correct out of 10")
print("It took you about", int(end_time - start_time), "seconds to do the problems")

# 5.10
import math

file = open("scores", "r")
i = 0
for line in file:
    fields = line.split(",")
    field1 = float(fields[0])
    field2 = str(fields[1])
    if field1 > i:
        i = field1
        x = field2
print(x, "has the highest score of", i, "%")

#5.28
import math
e = 0
i = 10000
while(i != 1000000):
    for k in range(i):
        e += (1/math.factorial(k))
    print("The answer for e when i is", i, "is", e)
    i += 10000
