# 11.1


matrix1 = list(map(float, input("Enter a 3 by 4 matrix for row 0: ").split()))
matrix2 = list(map(float, input("Enter a 3 by 4 matrix for row 1: ").split()))
matrix3 = list(map(float, input("Enter a 3 by 4 matrix for row 2: ").split()))

matrix = [matrix1, matrix2, matrix3]
for column in range(len(matrix[0])):
    total = 0
    for row in range(len(matrix)):
        total += matrix[row][column]
    print("Sum of the elements for column", column, "is", total)
print("-------------------------------------------------------------------------------------")
print()


# 11.3
# Grade exam
import operator
def main():



    answers = [
        ['A', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
        ['D', 'B', 'A', 'B', 'C', 'A', 'E', 'E', 'A', 'D'],
        ['E', 'D', 'D', 'A', 'C', 'B', 'E', 'E', 'A', 'D'],
        ['C', 'B', 'A', 'E', 'D', 'C', 'E', 'E', 'A', 'D'],
        ['A', 'B', 'D', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
        ['B', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
        ['B', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
        ['E', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D']]
    keys = ['D', 'B', 'D', 'C', 'C', 'D', 'A', 'E', 'A', 'D']
    scoreArray = {}

    for i in range(len(answers)): # Grade one student
        correctCount = 0
        for j in range(len(answers[i])):
            if answers[i][j] == keys[j]:
                correctCount += 1

        scoreArray.update({i: correctCount})
    sortedscoreArray = sorted(scoreArray.items(), key = operator.itemgetter(1))
    #print(sortedscoreArray)
    for student, score in sortedscoreArray:
        print("Student %d 's correct count is %d" %(student, score))


main()


print("------------------------------------------------------------------------------------")
print()


# 11.4

employees = [
    ["Employee 0", 2, 4, 3, 4, 5, 8, 8],
    ["Employee 1", 7, 3, 4, 3, 3, 4, 4],
    ["Employee 2", 3, 3, 4, 3, 3, 2, 2],
    ["Employee 3", 9, 3, 4, 7, 3, 4, 1],
    ["Employee 4", 3, 5, 4, 3, 6, 3, 8],
    ["Employee 5", 3, 4, 4, 6, 3, 4, 4],
    ["Employee 6", 3, 7, 4, 8, 3, 8, 4],
    ["Employee 7", 6, 3, 5, 9, 2, 7, 9]
]

list = []
for i in range(len(employees)):
    total = 0
    for j in range(1, len(employees[0])):
        total += employees[i][j]
    list.append(total)


employeeDict = {
    "employee 0": 0,
    "employee 1": 0,
    "employee 2": 0,
    "employee 3": 0,
    "employee 4": 0,
    "employee 5": 0,
    "employee 6": 0,
    "employee 7": 0,

}

for i in range(0, len(list)):
    employeeDict["employee %d" %i] = list[i]

print(employeeDict)

sort_employee = sorted(employeeDict.items(), key=lambda x: x[1], reverse=True)

for i in sort_employee:
    print(i[0], ":", i[1])

print("------------------------------------------------------------------------------------")
print()
# 11.8

def distance(x1, y1, x2, y2):
    return ((x2 - x1) * (x2 - x1) + (y2-y1) * (y2-y1)) ** 0.5

def closestPoints(points):
    p1, p2 = 0, 1
    distances = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = distance(points[i][0], points[i][1],
                points[j][0], points[j][1])
            distances.append([d, points[i][0], points[i][1], points[j][0], points[j][1]])

    distances.sort()
    for k in range(len(distances)):
        if distances[0][0] == distances[k][0]:
            print("(", distances[k][1], ',', distances[k][2], ")","(",distances[k][3], ",", distances[k][4], ")")
        else:
            break
    print("The closest distance is", distances[0][0])

def main():

    numberofPoints = eval(input("Enter the number of points: "))

    points = []
    print("Enter", numberofPoints, "points:")
    for i in range(numberofPoints):
        point = 2 * [0]
        point[0], point[1] = eval(input("Enter coordinates: "))
        points.append(point)

    print("The points that have the same minimum distance are: ")
    closestPoints(points)

main()





# 11.13
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