# 7.1

class Rectangle:
    def __init__(self, width = 1, height = 2):
        self.width = width
        self.height = height
    def getArea(self):
        return self.width * self.height
    def getPerimeter(self):
        return 2*self.width + 2*self.height

if __name__ == '__main__':
    rectangle1 = Rectangle(4, 40)
    print("Rectangle 1 Perimeter and Area:")
    print(rectangle1.getArea())
    print(rectangle1.getPerimeter())

    rectangle2 = Rectangle(3.5, 35.7)
    print("Rectangle 2 Perimeter and Area")
    print(rectangle2.getArea())
    print(rectangle2.getPerimeter())

