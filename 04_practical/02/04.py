def has_duplicates(list):
    length = len(list)
    i = 0
    while i < length:
        j = i + 1
        while j < length:
            if list[i] == list[j]:
                return True
            j += 1
        i += 1
    return False

numbers = [4, 7, 2, 4]
result = has_duplicates(numbers)
print("Contains duplicates:", result)
