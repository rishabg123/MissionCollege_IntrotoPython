def getRectangle(points):
    points = points.split()
    pts = []
    i = 0
    while i < len(points):
        pts.append((float(points[i]), float(points[i+1])))
        i+=2
    points = pts

    minX = min([x for (x,y) in points])
    maxX = max([x for (x, y) in points])
    minY = min([y for (x, y) in points])
    maxY = max([y for (x, y) in points])

    width = abs(maxX - minX)
    height = abs(maxY - minY)
    center = ((minX + maxX) / 2.0, (minY + maxY) / 2.0)

    print("The bounding rectangle is centered at", center, " with width", width, "and height ", height)

def main():
    getRectangle(str(input("Enter the points in one line seperated by a space: ")))
main()