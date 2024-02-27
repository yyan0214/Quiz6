import math


class Shape:
    def set_width(self, width):
        raise NotImplementedError("set_width method not implemented")

    def set_height(self, height):
        raise NotImplementedError("set_height method not implemented")

    def get_area(self):
        raise NotImplementedError("get_area method not implemented")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def set_width(self, width):
        self.radius = width / 2

    def set_height(self, height):
        self.radius = height / 2

    def get_area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return 0.5 * self.base * self.height

class Polygon(Shape):
    def __init__(self, sides, length):
        self.sides = sides
        self.length = length

    def get_area(self):
        # Implement area calculation for a polygon with n sides
        # For simplicity, assuming a regular polygon
        return 0.25 * self.sides * self.length ** 2 * (1 / math.tan(math.pi / self.sides))

def main():
    # Create instances of shapes
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    triangle = Triangle(3, 4)
    polygon = Polygon(6, 5)

    # Set dimensions for shapes
    circle.set_width(10)
    rectangle.set_height(8)

    # Calculate and print areas of shapes
    print("Area of Circle:", circle.get_area())
    print("Area of Rectangle:", rectangle.get_area())
    print("Area of Triangle:", triangle.get_area())
    print("Area of Polygon:", polygon.get_area())

if __name__ == "__main__":
    main()
