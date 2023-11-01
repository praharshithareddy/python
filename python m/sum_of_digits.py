def sum_of_digits(number):
    
    digit_sum = sum(int(digit) for digit in str(number))
    while digit_sum > 12:
        digit_sum = sum(int(digit) for digit in str(digit_sum))
    return digit_sum
N = int(input("Enter N value: "))
number = int(input(f"Enter {N} digit number: "))
result = sum_of_digits(number)
print(f"Sum of {N} digit number: {result}")
