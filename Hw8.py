# 8.3

def valid(password) -> str:
    digits = 0
    characters = 0

    for char in password:
        if char.isalpha():
            characters += 1
        elif char.isdigit():
            digits += 1
            characters += 1

    if characters >= 8:
        if digits >= 2:
            print("Password is valid")
        else:
            print("Password doesn't contain enough digits")
    else:
        print("Password doesn't contain enough characters")
    return ""


# 8.11

def reverse(s):
    char = []
    for i in range(len(s)):
        char.append(s[i])
    char.reverse()
    for i in char:
        print(i, end='')
    return ""

# 8.2

def findStr(str1, str2) -> bool:
    if str1.find(str2) != -1:
        return True
    else:
        return False


# 8.7

def getNumber(c):

    if(c=='a' or c== 'b' or c=='c' or c=='A' or c == 'B' or c == 'C'):
        return (2)

    elif(c=='d' or c== 'e' or c=='f' or c=='D' or c == 'E' or c == 'F'):
        return (3)

    elif(c=='g' or c== 'h' or c=='i' or c=='G' or c == 'H' or c == 'I'):
        return (4)
    elif(c=='j' or c== 'k' or c=='l' or c=='J' or c == 'K' or c == 'L'):
        return (5)
    elif(c=='m' or c== 'n' or c=='o' or c=='M' or c == 'N' or c == 'O'):
        return (6)
    elif(c=='p' or c== 'q' or c=='r' or c=='s' or c=='P' or c == 'Q' or c == 'R' or c == 'S'):
        return (7)
    elif(c=='t' or c== 'u' or c=='v' or c=='T' or c == 'U' or c == 'V'):
        return (8)

    elif(c=='w' or c== 'x' or c=='y' or c=='z' or c=='W' or c == 'X' or c == 'Y' or c == 'Z'):
        return (9)
    else:
        return (0)

# 8.10

def decimalToBinary(n):
    return bin(n).replace("0b", "")


if __name__ == '__main__':
    print("Enter a password: ", end='')
    password = str(input())
    print(valid(password), end='')
    print("---------------------------------------------------------------------------")
    print("Enter a string to reverse")
    reversal = str(input())
    print(reverse(reversal))
    print("---------------------------------------------------------------------------")
    print("Enter String Number 1: ", end='')
    str1 = str(input())
    print("Enter String Number 2: ", end='')
    str2 = str(input())
    if findStr(str1, str2) == True:
        print("String 1 and String 2 are part of each other")
    else:
        print("String 1 is not a part of String 2")

    print("---------------------------------------------------------------------------")

    string = input("Please enter any string to convert: ")
    length = len(string)
    for i in range(length):

        c = string[i]
        k = getNumber(c)

        if (k == 0):
            print(c, end="")
        else:
            print(k, end="")
    print("")
    print("---------------------------------------------------------------------------")

    print("Enter a decimal to convert to binary: ", end='')
    number = int(input())
    print("The binary equivalent of", number, "is:", decimalToBinary(number))



