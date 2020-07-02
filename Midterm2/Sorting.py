# Selection Sort

def selectionSort(list):
    for i in range(0, len(list) - 1):
        currentMin = list[i]
        currentMinIndex = i
        for j in range(i+1, len(list)):
            if currentMin > list[j]:
                currentMin = list[j]
                currentMinIndex = j
        if currentMinIndex != i:
            list[currentMinIndex] = list[i]
            list[i] = currentMin
    return list



# Insertion Sort

def insertionSort(list):
    for i in range(1, len(list)):
        currentElement = list[i]
        k = i-1
        while k >= 0 and list[k] > currentElement:
            list[k+1] = list[k]
            k -= 1
        list[k+1] = currentElement
    return list

if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6]
    print(selectionSort(arr))
    # arr = [12, 11, 13, 5, 6, 7]
    # print(insertionSort(arr))