import numpy as np
from numpy import unravel_index
def locateLargest():
    twoDArray = [

    ]
    print("Enter the number of rows in the list: ", end='')
    numRows = int(input())
    tempList = []
    for i in range(numRows):
        tempList.clear()
        var = numRows - i
        twoDArray.insert(0, input("Enter a row-%d: " %var).split())

    twoDArray = np.array(twoDArray).astype(np.float)
    print("The location of the largest value is:", unravel_index(twoDArray.argmax(), twoDArray.shape))
    return ""

if __name__ == '__main__':
    print(locateLargest())