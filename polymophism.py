class Shape:
    def draw(self):
        print("Drawing a shape")

class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle")

class Square(Rectangle):
    def draw(self):
        print("Drawing a square")

# Create instances and call their draw methods
shape = Shape()
rectangle = Rectangle()
square = Square()

shape.draw()
rectangle.draw()
square.draw()
