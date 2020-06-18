class Rectangle:
    def __init__(self, width, height):
        self.__init__(width)
        self.__init__(height)
    def getArea(self):
        if self.height == None or self.width == None:
            self.height = 2
            self.width = 1

        return self.width * self.height
    def getPerimeter(self):
        if self.height == None or self.width == None:
            self.height = 2
            self.width = 1
        return 2 * self.width + (2 * self.height)