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