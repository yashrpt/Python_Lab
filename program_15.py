
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __eq__(self, other):
        return self.area() == other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __str__(self):
        return f"Circle with radius {self.radius}, Area = {self.area():.2f}"


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


# Create circles
c1 = Circle(5)
c2 = Circle(3)

print("Circle 1:", c1)
print("Circle 2:", c2)
print("Area of Circle 1:", round(c1.area(), 2))
print("Area of Circle 2:", round(c2.area(), 2))
print("Circle 1 smaller than Circle 2:", c1 < c2)
print("Circles have equal areas:", c1 == c2)

# Create vectors
v1 = Vector(2, 3)
v2 = Vector(4, 5)

print("\nVector 1:", v1)
print("Vector 2:", v2)
print("Vector Addition:", v1 + v2)
print("Vectors are equal:", v1 == v2)
