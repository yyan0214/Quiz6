from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

class ShapeFactory:
    @staticmethod
    def create_shape(shape_type, *args):
        if shape_type == "circle":
            return Circle(*args)
        elif shape_type == "square":
            return Square(*args)
        elif shape_type == "rectangle":
            return Rectangle(*args)
        else:
            raise ValueError("Invalid shape type")

def main():
    # Create instances of different shapes using the factory method
    shapes = [
        ShapeFactory.create_shape("circle", 5),
        ShapeFactory.create_shape("square", 4),
        ShapeFactory.create_shape("rectangle", 3, 6)
    ]

    # Calculate and print the areas of the shapes
    for shape in shapes:
        print(f"Area of {type(shape).__name__}: {shape.get_area()}")

if __name__ == "__main__":
    main()
