def binaryToDecimal(binaryString):
    return int(binaryString, 2)

if __name__ == '__main__':
    print("Enter a binary value to be converted into a decimal: ", end='')
    binaryString = str(input())
    print("The binary number is", binaryToDecimal(binaryString))