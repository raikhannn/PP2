#1
class StringManipulator:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("Enter a string: ")

    def printString(self):
        print("String in uppercase:", self.input_string.upper())

# Example usage:
manipulator = StringManipulator()
manipulator.getString()
manipulator.printString()

#2
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length * self.length

# Example usage:
shape = Shape()
print("Area of Shape:", shape.area())

square = Square(5)
print("Area of Square:", square.area())

#3
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length * self.length

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Example usage:
square = Square(5)
print("Area of Square:", square.area())

rectangle = Rectangle(4, 6)
print("Area of Rectangle:", rectangle.area())

#4
import math
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def show(self):
        print("Coordinates of the point: ({}, {})".format(self.x, self.y))
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    def dist(self, other_point):
        distance = math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
        return distance
# Example usage:
point1 = Point(3, 4)
point2 = Point(6, 8)
point1.show()
point2.show()
print("Distance between the points:", point1.dist(point2))
# Move point1 to a new location
point1.move(1, 2)
point1.show()

#5
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} successfully.")
        else:
            print("Invalid deposit amount. Amount must be greater than 0.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount} successfully.")
            else:
                print("Insufficient funds. Withdrawal amount exceeds available balance.")
        else:
            print("Invalid withdrawal amount. Amount must be greater than 0.")
# Example usage:
account = Account("John Doe", 1000)
print("Account owner:", account.owner)
print("Initial balance:", account.balance)
account.deposit(500)
print("Current balance after deposit:", account.balance)
account.withdraw(200)
print("Current balance after withdrawal:", account.balance)
account.withdraw(1500)  # Attempt to withdraw more than available balance

#6
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
# Example list
numbers = [2, 3, 5, 7, 11, 13, 17, 19, 20, 23]
# Filter prime numbers
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print("Prime numbers in the list:", prime_numbers)

