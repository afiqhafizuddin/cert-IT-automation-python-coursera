# Linear Search
def linear_search(list, key):
    """If key is in the list, returns its postion in the list, otherwise returns -1
    """

    for i, item in enumerate(list):
        if item == key:
            return i
    return -1

# binary search
def binary_seacrh(list, key):
    """returns the position of key in the list if found, otherwise returns -1
    """

    left = 0
    right = len(list) - 1
    while left <= right:
        middle = (left + right) // 2

        if list[middle] == key:
            return middle
        if list[middle] > key:
            right = middle - 1
        if list[middle] < key:
            left = middle + 1
    return -1

name = ['michael', 'steven', 'gerrard', 'mo salah', 'Afiq', 'sadio', 'mane']

print(linear_search(name, 'Afiq'))

print(binary_seacrh(sorted(name), 'Afiq'))