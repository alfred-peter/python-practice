def sum_of_digits(number):
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number = number // 10
    return total


num = 67
print(sum_of_digits(num)) 