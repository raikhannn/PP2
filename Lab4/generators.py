#1
def squares_up_to_N(N):
    for i in range(1, N + 1):
        yield i ** 2
# Example usage
N = 5
squares_generator = squares_up_to_N(N)
# Print the squares
for square in squares_generator:
    print(square)

#2
def even_numbers_up_to_n(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i
def main():
    try:
        n = int(input("Enter the value of n: "))
        if n < 0:
            print("Please enter a non-negative integer.")
            return
        even_generator = even_numbers_up_to_n(n)
        even_numbers_str = ', '.join(map(str, even_generator))
        print("Even numbers up to", n, ":", even_numbers_str)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
if __name__ == "__main__":
    main()

#3
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
# Example usage
def main():
    try:
        n = int(input("Enter the value of n: "))
        if n < 0:
            print("Please enter a non-negative integer.")
            return
        print("Numbers divisible by 3 and 4 up to", n, ":")
        for num in divisible_by_3_and_4(n):
            print(num, end=" ")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
if __name__ == "__main__":
    main()

#4
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2
# Test the generator with a for loop
def main():
    try:
        a = int(input("Enter the starting number (a): "))
        b = int(input("Enter the ending number (b): "))
        
        print(f"Squares of numbers from {a} to {b}:")
        for square in squares(a, b):
            print(square)
    except ValueError:
        print("Invalid input. Please enter valid integers.")
if __name__ == "__main__":
    main()

#5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1
# Test the generator with a for loop
def main():
    try:
        n = int(input("Enter a number (n): "))
        print("Counting down from", n, "to 0:")
        for num in countdown(n):
            print(num)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
if __name__ == "__main__":
    main()
