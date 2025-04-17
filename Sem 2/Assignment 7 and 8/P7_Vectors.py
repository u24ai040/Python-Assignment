# QUESTION 7

import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def angle_with_x_axis(self):
        return math.degrees(math.atan2(self.y, self.x))

    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y

    def cross_product(self, other):
        return self.x * other.y - self.y * other.x

    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"

class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross_product(self, other):
        return Vector3D(self.y * other.z - self.z * other.y,
                        self.z * other.x - self.x * other.z,
                        self.x * other.y - self.y * other.x)

    def __repr__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"

print("Enter 2D Vector 1 (x, y):")
x1 = float(input("x1: "))
y1 = float(input("y1: "))
print("Enter 2D Vector 2 (x, y):")
x2 = float(input("x2: "))
y2 = float(input("y2: "))

Vector_2D_1 = Vector2D(x1, y1)
Vector_2D_2 = Vector2D(x2, y2)

print("2D Magnitude:", Vector_2D_1.magnitude())
print("2D Angle with X-axis:", Vector_2D_1.angle_with_x_axis())
print("2D Distance:", Vector_2D_1.distance(Vector_2D_2))
print("2D Dot Product:", Vector_2D_1.dot_product(Vector_2D_2))
print("2D Cross Product:", Vector_2D_1.cross_product(Vector_2D_2))

print("Enter 3D Vector 1 (x, y, z):")
x1 = float(input("x1: "))
y1 = float(input("y1: "))
z1 = float(input("z1: "))

print("Enter 3D Vector 2 (x, y, z):")
x2 = float(input("x2: "))
y2 = float(input("y2: "))
z2 = float(input("z2: "))

Vector_3D_1 = Vector3D(x1, y1, z1)
Vector_3D_2 = Vector3D(x2, y2, z2)
print("3D Magnitude:", Vector_3D_1.magnitude())
print("3D Distance:", Vector_3D_1.distance(Vector_3D_2))
print("3D Dot Product:", Vector_3D_1.dot_product(Vector_3D_2))
print("3D Cross Product:", Vector_3D_1.cross_product(Vector_3D_2))
