import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, point:object):
        x1 = self.x
        y1 = self.y
        x2 = point.x
        y2 = point.y

        dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        return dist



if __name__ == '__main__':
    point = Point(5,0)
    point1 = Point(10,0)
    print(point.distance(point1))