#1
def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

#2
def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

# Read Fahrenheit temperature from the user
fahrenheit_temperature = float(input("Enter the temperature in Fahrenheit: "))

# Convert Fahrenheit to Celsius
celsius_temperature = fahrenheit_to_celsius(fahrenheit_temperature)

# Display the equivalent Celsius temperature
print(f"The equivalent temperature in Celsius is: {celsius_temperature:.2f}°C")

#3
def solve(numheads, numlegs):
    # Calculate number of rabbits
    rabbits = (numlegs - 2 * numheads) / 2
    # Calculate number of chickens using the equation c = numheads - r
    chickens = numheads - rabbits
    # Check if the calculated values are valid
    if chickens < 0 or rabbits < 0 or chickens % 1 != 0 or rabbits % 1 != 0:
        return "No solution exists."
    else:
        return int(chickens), int(rabbits)
# Example usage:
numheads = 35
numlegs = 94
result = solve(numheads, numlegs)
print("Number of chickens and rabbits:", result)

#4
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True
def filter_prime(numbers):
    prime_numbers = filter(is_prime, numbers)
    return list(prime_numbers)

#5
from itertools import permutations
def print_permutations(string):
    # Generate all permutations of the string
    perms = permutations(string)
    # Print each permutation
    for perm in perms:
        print(''.join(perm))

#6
def reverse_sentence(sentence):
    # Split the sentence into words
    words = sentence.split()
    # Reverse the order of the words
    reversed_words = words[::-1]
    # Join the words back into a sentence
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

#7
def has_33(nums):
    # Iterate through the list, except for the last element
    for i in range(len(nums) - 1):
        # Check if the current element and the next element are both 3
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

#8
def spy_game(nums):
    # Initialize variables to keep track of positions of 0, 0, and 7
    pos_0 = None
    pos_1 = None
    pos_2 = None
    # Iterate through the list
    for i, num in enumerate(nums):
        if num == 0:
            if pos_0 is None:
                pos_0 = i
            elif pos_1 is None:
                pos_1 = i
        elif num == 7:
            if pos_2 is None:
                pos_2 = i    
    # Check if all three positions are found and in order
    if pos_0 is not None and pos_1 is not None and pos_2 is not None and pos_0 < pos_1 < pos_2:
        return True
    else:
        return False
    
#9
import math
def sphere_volume(radius):
    volume = (4/3) * math.pi * radius**3
    return volume

#10
def unique_elements(input_list):
    unique_list = []
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

#11
def is_palindrome(word):
    # Convert the word to lowercase and remove spaces
    word = word.lower().replace(" ", "")
    # Check if the word is equal to its reverse
    return word == word[::-1]

#12
def histogram(numbers):
    for num in numbers:
        print('*' * num)
# Example usage:
numbers = [4, 9, 7]
histogram(numbers)

#13
import random
def guess_the_number():
    # Generate a random number between 1 and 20
    secret_number = random.randint(1, 20)
    guesses = 0
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    while True:
        print("Take a guess.")
        guess = int(input())
        guesses += 1
        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break
# Call the function to start the game
guess_the_number()     