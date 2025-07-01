def find_max(list):
    if not list:
        return None
    max_value = list[0]
    for num in list:
        if num > max_value:
            max_value = num
    return max_value

numbers = [20, 17, 19, 21]
result = find_max(numbers)
print("The maximum number is:", result)
