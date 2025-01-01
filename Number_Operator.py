def check_square(number):
    root = pow(number, 0.5)  # Same as root = number ** 0.5
    return root.is_integer()  # Check if the square root is an integer


def check_cube(number):
    root = round(pow(number, 1 / 3))  # Same as root = number ** (1/3)
    return pow(root, 3) == number  # Recalculate the cube to ensure accuracy


def check_prime(number):
    if number <= 1:  # Numbers <= 1 are not prime
        return False

    divisor_count = 0  # Initialize the count of divisors
    for i in range(1, number + 1):  # Iterate from 1 to the number itself
        if number % i == 0:  # Check if 'i' is a divisor of 'number'
            divisor_count += 1  # Increment the divisor count

    return divisor_count == 2  # Returns True if the number has exactly 2 divisors


def check_palindrome(number):
    if number > 9:  # Only check for numbers with at least two digits
        return str(number) == str(number)[::-1]  # Compare the original and reversed strings
    return False  # Numbers less than 10 cannot be palindromes


def check_armstrong(number):
    if number < 10:  # Single-digit numbers are not valid for Armstrong check
        return "Error! Invalid single-digit number."

    digits = [int(d) for d in str(number)]  # Split the number into its individual digits
    num_digits = len(digits)  # Count the number of digits in the number

    armstrong_sum = 0  # Initialize the sum of digits

    for d in digits:
        armstrong_sum += pow(d, num_digits)  # Add each digit raised to the power of num_digits

    return armstrong_sum == number  # Compare the sum with the original number