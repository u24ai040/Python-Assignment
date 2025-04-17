# QUESTION 5

import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length+ self.width)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius


while True:
        print("\nChoose a Shape:")
        print("1. Rectangle")
        print("2. Circle")
        print("3. Exit")

        choice = input("Enter your choice from 1 to 3: ")

        if choice == '1':
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            rect = Rectangle(length, width)
            print(f"Area: {rect.area()}")
            print(f"Perimeter: {rect.perimeter()}")

        elif choice == '2':
            radius = float(input("Enter the radius of the circle: "))
            circ = Circle(radius)
            print(f"Area: {circ.area():.2f}")
            print(f"Perimeter (Circumference): {circ.perimeter():.2f}")

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please try again.")
