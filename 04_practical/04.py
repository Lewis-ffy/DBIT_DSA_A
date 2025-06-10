def sum_tail(n, total=0):
    
    if n == 0:
        return total
    return sum_tail(n - 1, total + n)

print(sum_tail(5))  # Output: 15
