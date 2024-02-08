numbers = [20, 36, 12, 24, 20, 48, 74, 353, 23, 98]

for number in range(len(numbers)):
    if numbers[number] == 353:
        numbers[number] = 35

numbers.sort()
print("Largest number in numbers list is", numbers[-1])
