# 12.1

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
    def getArea(self):
        s = (self.side1+self.side2+self.side3)/2
        area = math.sqrt(s*(s-self.side1) * (s-self.side2) * (s-self.side3))
        return area
    def getPerimeter(self):
        return self.side1 + self.side2 + self.side3
    def __str__(self):
        return "Triangle: side1 = " + str(self.side1) + " side2 = " + str(self.side2) + " side3 = " + str(self.side3)



# 12.4

# def getRectangle(points):
#     points = points.split()
#     pts = []
#     i = 0
#     while i < len(points):
#         pts.append((float(points[i]), float(points[i+1])))
#         i+=2
#     points = pts
#
#     minX = min([x for (x,y) in points])
#     maxX = max([x for (x, y) in points])
#     minY = min([y for (x, y) in points])
#     maxY = max([y for (x, y) in points])
#
#     width = abs(maxX - minX)
#     height = abs(maxY - minY)
#     center = ((minX + maxX) / 2.0, (minY + maxY) / 2.0)
#
#     print("The bounding rectangle is centered at", center, " with width", width, "and height ", height)
#
# def main():
#     getRectangle(str(input("Enter the points in one line seperated by a space: ")))
# main()

if __name__ == '__main__':
    print("Enter side 1 of the triangle: ", end='')
    side1 = float(input())
    print("Enter side 2 of the triangle: ", end='')
    side2 = float(input())
    print("Enter side 3 of the triangle: ", end='')
    side3 = float(input())
    print("Enter the color of the triangle: ", end='')
    color = str(input())
    print("Enter 0 if you don't want the triangle filled and 1 if you want it filled: ", end='')
    filled = int(input())
    triangle = Triangle(side1, side2, side3)
    print(triangle.__str__())
    print("The area of the triangle is:", triangle.getArea())
    print("The perimeter of the triangle is:", triangle.getPerimeter())
    print("The color of the triangle is", color)
    if filled == 0:
        print("The triangle is not filled")
    else:
        print("The triangle is filled")