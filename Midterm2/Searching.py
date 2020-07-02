# Linear Search

def linearSearch(arr, find):
    for i in arr:
        if i == find:
            return True
    return False


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

if __name__ == '__main__':
    arr1 = [2, 3, 10, 20, 30]
    if linearSearch(arr1, 3) == True:
        print("Element is present in the array")
    else:
        print("Element is not present in the array")

    arr = [2, 3, 4, 10, 40]
    x = 5
    result = binary_search(arr, x)
    if result != -1:
        print("Element is present at index", str(result))
    else:
        print("Element is not present in array")