def calculate_statistics(numbers):
    total = 0
    for number in numbers:
        total += number
    mean = total / len(numbers)
    max_value = numbers[0]
    min_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number
        if number < min_value:
            min_value = number
    return total, mean, max_value, min_value

numbers = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
total, mean, max_value, min_value = calculate_statistics(numbers)
print("Total:", total)
print("Mean:", mean)
print("Maximum:", max_value)
print("Minimum:", min_value)