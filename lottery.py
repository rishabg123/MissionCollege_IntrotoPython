import random
print("Enter digit 1")
digit1 = int(input())
print("Enter digit 2")
digit2 = int(input())


realDigit1 = random.randint(0,9)
realDigit2 = random.randint(0,9)

if (digit1 == realDigit1 and digit2 == realDigit2):
    print("You won 10,000")
elif(digit1 == realDigit2 and digit2 == realDigit1):
    print("you won 3000")
elif(digit1 == realDigit2 or digit2 == realDigit1):
    print("you won 1000")
else:
    print("You won nothing :(")
