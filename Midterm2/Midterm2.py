# Question 1

class LinearEquation:
    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
    def getA(self):
        return self.a
    def getB(self):
        return self.b
    def getC(self):
        return self.c
    def getD(self):
        return self.d
    def getE(self):
        return self.e
    def getF(self):
        return self.f
    def setA(self, new):
        self.a = new
    def setB(self, new):
        self.b = new
    def setC(self, new):
        self.c = new
    def setD(self, new):
        self.d = new
    def setE(self, new):
        self.e = new
    def setF(self, new):
        self.f = new
    def isSolvable(self):
        x = ((self.e * self.d) - (self.b * self.f) / (self.a * self.d) - (self.b * self.c))
        y = ((self.a * self.f) - (self.e * self.c) / (self.a * self.d) - (self.b * self.c))
        det = (self.a * self.d) - (self.c * self.b)
        if det == 0:
            return False
        else:
            return True
    def getX(self):
        x = ((self.e * self.d) - (self.b * self.f) / (self.a * self.d) - (self.b * self.c))

        return x

    def getY(self):
        y = ((self.a * self.f) - (self.e * self.c) / (self.a * self.d) - (self.b * self.c))
        return y




# Question 2

x1 = float(input("Enter a point for x1: "))
y1 = float(input("Enter a point for y1: "))
x2 = float(input("Enter a point for x2: "))
y2 = float(input("Enter a point for y2: "))
x3 = float(input("Enter a point for x3: "))
y3 = float(input("Enter a point for y3: "))
x4 = float(input("Enter a point for x4: "))
y4 = float(input("Enter a point for y4: "))

slope1 = (y2-y1) / (x2-x1)
slope2 = (y4-y3) / (x4 - x3)
a = -slope1
d = -slope2
b = 1
e = 1
c = y1 - ((slope1) * x1)
f = y3 - ((slope2) * x3)

equation = LinearEquation(a, b, c, d, e, f)
print(equation.getX())
print(equation.getY())



# Question 3
import math

class Point:
    def __init__(self, x=0, y =0):
        self.x = x
        self.y = y

    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def distance(self, point:object):
        x1 = self.x
        y1 = self.y
        x2 = point.x
        y2 = point.y

        dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

        return dist
    def isNearby(self, p1:object):
       x1 = self.x
       y1 = self.y
       x2 = p1.x
       y2 = p1.y
       distP1  = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

       if distP1 < 5:
           return True
       else:
           return False

     
    def __str__(self):
        return 'Point(x='+str(self.x)+', y='+str(self.y)+ ')'


# Question 4




# Question 5



if __name__ == '__main__':
    linearEquation = LinearEquation(2,1,5,-1,1,2)
    linearEquation2 = LinearEquation(1,1,2,2,0,0)
    print("The a is: ", linearEquation.getA())
    print("The b is: ", linearEquation.getB())
    print("The c is: ", linearEquation.getC())
    print("The d is: ", linearEquation.getD())
    print("The e is: ", linearEquation.getE())
    print("The f is: ", linearEquation.getF())

    if linearEquation.isSolvable() == False:
        print("This equation cannot be solved")
    else:
        print("This equation can be solved")
        print("The solution for X is", linearEquation.getX())
        print("The solution for Y is", linearEquation.getY())

    print("---------------------------------------------------------------")
    print("The a is: ", linearEquation2.getA())
    print("The b is: ", linearEquation2.getB())
    print("The c is: ", linearEquation2.getC())
    print("The d is: ", linearEquation2.getD())
    print("The e is: ", linearEquation2.getE())
    print("The f is: ", linearEquation2.getF())

    if linearEquation2.isSolvable() == False:
        print("This equation cannot be solved")
    else:                                                     
        print("This equation can be solved")
        print("The solution for X is", linearEquation2.getX())
        print("The solution for Y is", linearEquation2.getY())

    print("---------------------------------------------------------------")

    point1 = Point(2, 5)
    point2 = Point(3, 10)
    point3 = Point(2,6)

    print("Point 1's X value is", point1.getX())
    print("Point 1's Y value is", point1.getY())
    print("Point 2's X value is", point2.getX())
    print("Point 2's Y value is", point2.getY())
    print("Point 3's X value is", point3.getX())
    print("Point 3's Y value is", point3.getY())


    print("The distance between Point 1 and Point 2 is", point1.distance(point2))
    if point1.isNearby(point2) == True:
        print("Point 1 is close to Point 2")
    else:
        print("Point 1 is not close to Point 2")

    if point1.isNearby(point3) == True:
        print("Point 1 is close to Point 3")
    else:
        print("Point 1 is not close to Point 3")

    print(str(point1))
    print(str(point2))
    print(str(point3))
        