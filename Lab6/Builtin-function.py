#1
from functools import reduce

def multiply_list(numbers):
    # Using reduce to multiply all numbers in the list
    result = reduce(lambda x, y: x * y, numbers)
    return result

# Example usage
numbers = [1, 2, 3, 4, 5]
result = multiply_list(numbers)
print("Multiplication result:", result)

#2
def count_upper_lower(string):
    # Initializing counts for upper and lower case letters
    upper_count = 0
    lower_count = 0
    # Iterating through each character in the string
    for char in string:
        # Checking if the character is upper case
        if char.isupper():
            upper_count += 1
        # Checking if the character is lower case
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count
# Example usage
input_string = input("Enter a string: ")
upper, lower = count_upper_lower(input_string)
print("Number of upper case letters:", upper)
print("Number of lower case letters:", lower)

#3
def is_palindrome(string):
    # Removing spaces and converting to lowercase for case-insensitive comparison
    cleaned_string = string.replace(" ", "").lower()
    # Reversing the string
    reversed_string = cleaned_string[::-1]
    # Checking if the original string is equal to its reverse
    return cleaned_string == reversed_string
# Example usage
input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

#4
import time
import math
def calculate_square_root(number, milliseconds):
    time.sleep(milliseconds / 1000)  # Convert milliseconds to seconds
    square_root = math.sqrt(number)
    return square_root
def main():
    number = int(input("Enter the number: "))
    milliseconds = int(input("Enter the delay in milliseconds: "))
    result = calculate_square_root(number, milliseconds)
    print(f"Square root of {number} after {milliseconds} milliseconds is {result}")
if __name__ == "__main__":
    main()

#5
def all_elements_true(tuple_values):
    return all(tuple_values)
# Example usage
tuple_values = (True, True, True)
print("All elements true?", all_elements_true(tuple_values))
tuple_values = (True, False, True)
print("All elements true?", all_elements_true(tuple_values))
