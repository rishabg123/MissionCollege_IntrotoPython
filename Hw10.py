# 10.1

input_string = input("Enter all the scores of the students: ")
print("\n")
scores = input_string.split()
newScores = []
for i in scores:
    newScores.append(int(i))

best_score = newScores[0]
for i in range(1, len(newScores)):
    if newScores[i] > best_score:
        best_score = newScores[i]
letter_grades = []
for i in range(0, len(newScores)):
    if (newScores[i] >= best_score - 10):
        letter_grades.append("A")
    elif(newScores[i] >= best_score - 20):
        letter_grades.append("B")
    elif (newScores[i] >= best_score - 30):
        letter_grades.append("C")
    elif (newScores[i] >= best_score - 40):
        letter_grades.append("D")
    else:
        letter_grades.append("F")

for i in range(0, len(newScores)):
    print("Student", i , "score is", newScores[i], "and their letter grade is", letter_grades[i])

print("-----------------------------------------------------------------------------------")
print()


# 10.8

nums = list(map(int, input("Enter numbers to get the lowest index of: ").split()))
index = nums.index(min(nums))
print("The smmallest number is", min(nums), "at index", index)

print("-----------------------------------------------------------------------------------")
print()

# 10.4

input_string = input("Enter all the scores, seperated by a space, to see how many are lower, equal to, or above the average: ")
print("\n")
userList = input_string.split()
scores2 = []
sum = 0
for i in userList:
    scores2.append(float(i))
    sum += float(i)
avg = sum / len(scores2)
aboveCount = 0
equalCount = 0
belowCount = 0
for i in scores2:
    if i > avg:
        aboveCount += 1
    elif i == avg:
        equalCount += 1
    else:
        belowCount += 1

print("The average is", avg)
print("There are", belowCount, "scores lower than the average")
print("There are", equalCount, "scores equal than the average")
print("There are", aboveCount, "scores higher than the average")

print("-----------------------------------------------------------------------------------")
print()

# 10.13

input_string = input("Enter all the numbers seperated by a space to find/remove the duplicates: ")
print("\n")
duplicate = input_string.split()
duplicate2 = []

for i in duplicate:
    duplicate2.append(float(i))

final = []
final = list(set(duplicate2))
print("The distinct numbers are:  ", end='')
print(final)
print()

print("-----------------------------------------------------------------------------------")
print()

# 10.26

input_string = input("Enter list number 1: ")
print("\n")
preList = input_string.split()
input_string = input("Enter list number 2: ")
print("\n")
preList2 = input_string.split()

list1 = []
list2 = []

for i in preList:
    list1.append(float(i))
for i in preList2:
    list2.append(float(i))
newList = []


while list1 != [] and list2 != []:
    if list1[0] < list2[0]:
        newList.append(list1.pop(0))
    else:
        newList.append(list2.pop(0))

newList += list1 + list2

print(newList)
