class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


# Function expecting a Shape and calculating area
def calculate_area(shape):
    return shape.area()


if __name__ == '__main__':
    rectangle = Rectangle(4, 5)
    square = Square(4)

    print(f"Rectangle Area: {calculate_area(rectangle)}")  # Output: Rectangle Area: 20
    print(f"Square Area: {calculate_area(square)}")  # Output: Square Area: 16
