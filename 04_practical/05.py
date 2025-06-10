text = "data structures and algorithms"
counts = {}

for letter in text:
    if letter in counts:
        counts[letter] = counts[letter] + 1
    else:
        counts[letter] = 1

print(counts)
