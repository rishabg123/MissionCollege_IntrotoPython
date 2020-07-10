
class GeometricObject:
    def __init__(self, color = "green", filled = True):
        self.__color = color
        self.__filled = filled
        def getColor(self):
            return  self.__color
        def setColor(self, color):
            self.__color =  color
        def isFilled(self):
            return  self.__filled
        def setFilled(self, filled):
            self.__filled  =  filled
        def __str__(self):
            return color + self.__color + "and filled: " + str(self.__filled)

import math
class Triangle(GeometricObject):
    def __init__(self, side1:float = 1.0, side2:float = 1.0, side3:float = 1.0):
        super().__init__()
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def getSide1(self):
        return self.side1
    def getSide2(self):
        return self.side2
    def getSide3(self):
        return self.side3

    def setSide1(self, side1:float):
        self.side1 = side1
    def setSide2(self, side2:float):
        self.side2 = side2
    def setSide3(self, side3:float):
        self.side3 = side3
    def getArea(self):
        s = (self.side1+self.side2+self.side3)/2
        area = math.sqrt(s*(s-self.side1) * (s-self.side2) * (s-self.side3))
        return area
    def isValid(self):
        if self.side1 + self.side2 < self.side3 or self.side2 + self.side3 < self.side1 or self.side1 + self.side3 < self.side2:
            raise RuntimeError('Not a valid triangle')

        else:
            return True
    def getPerimeter(self):
        return self.side1 + self.side2 + self.side3
    def __str__(self):
        return "Triangle: side1 = " + str(self.side1) + " side2 = " + str(self.side2) + " side3 = " + str(self.side3)

if __name__ == '__main__':
    print("Enter side 1 of the triangle: ", end='')
    side1 = float(input())
    print("Enter side 2 of the triangle: ", end='')
    side2 = float(input())
    print("Enter side 3 of the triangle: ", end='')
    side3 = float(input())
    # print("Enter the color of the triangle: ", end='')
    # color = str(input())
    # print("Enter 0 if you don't want the triangle filled and 1 if you want it filled: ", end='')
    # filled = int(input())
    triangle = Triangle(side1, side2, side3)
    print()
    try:
        triangle.isValid()
        print(triangle.__str__())
        print("The area of the triangle is:", triangle.getArea())
        print("The perimeter of the triangle is:", triangle.getPerimeter())
    except RuntimeError:
        print("Runtime Error: The triangle is not valid")


       # print("The color of the triangle is", color)
       #  if filled == 0:
       #      print("The triangle is not filled")
       #  else:
       #      print("The triangle is filled")