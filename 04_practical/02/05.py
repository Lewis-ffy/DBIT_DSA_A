def linear_search(list, target):
    index = 0
    while index < len(list):
        if list[index] == target:
            return index
        index += 1
    return -1

numbers = [10, 20, 30, 40, 50]
result = linear_search(numbers, 30)
print("Found at index:", result)
