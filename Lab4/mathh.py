#1
import math
def degree_to_radian(degree):
    return degree * math.pi / 180
# Test the function
def main():
    try:
        degree = float(input("Input degree: "))
        radian = degree_to_radian(degree)
        print("Output radian:", radian)
    except ValueError:
        print("Invalid input. Please enter a valid degree value.")
if __name__ == "__main__":
    main()

#2
def trapezoid_area(height, base1, base2):
    return (base1 + base2) * height / 2
# Test the function
def main():
    try:
        height = float(input("Height: "))
        base1 = float(input("Base, first value: "))
        base2 = float(input("Base, second value: "))
        area = trapezoid_area(height, base1, base2)
        print("Expected Output:", area)
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")
if __name__ == "__main__":
    main()

#3
import math
def polygon_area(num_sides, side_length):
    return (num_sides * side_length ** 2) / (4 * math.tan(math.pi / num_sides))
# Test the function
def main():
    try:
        num_sides = int(input("Input number of sides: "))
        side_length = float(input("Input the length of a side: "))
        
        area = polygon_area(num_sides, side_length)
        print("The area of the polygon is:", area)
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")
if __name__ == "__main__":
    main()

#4
def parallelogram_area(base_length, height):
    return base_length * height
# Test the function
def main():
    try:
        base_length = float(input("Length of base: "))
        height = float(input("Height of parallelogram: "))
        
        area = parallelogram_area(base_length, height)
        print("Expected Output:", area)
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")
if __name__ == "__main__":
    main()
