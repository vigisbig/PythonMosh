numbers = [3,5,7,9,3,5,6]
unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)
