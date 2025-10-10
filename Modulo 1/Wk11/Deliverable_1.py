# Class named circle, with a default attribute and a method that contian a formula
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_circle_area(self):
        area = (3.14 * self.radius ** 2)
        return area

circle = Circle(4)
area = circle.get_circle_area()

print(area)

