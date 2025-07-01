def find_min(list):
    if not list:
        return None
    min_value = list[0]
    for num in list:
        if num < min_value:
            min_value = num
    return min_value

numbers = [10, 41, 21, 11]
result = find_min(numbers)
print("The minimum number is:", result)
