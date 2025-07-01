def sum_of_elements(list):
    total = 0
    for num in list:
        total += num
    return total

numbers = [3, 7, 2, 8]
result = sum_of_elements(numbers)
print("The sum of elements is:", result)
