input_string = input("Enter list elements with space ")

inputList = input_string.split()


# Reversing a list using reversed()
def reverse_list(lst):
    return [number for number in reversed(lst)]


print(reverse_list(inputList))