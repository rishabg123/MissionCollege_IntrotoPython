# 7.1

class Rectangle:
    def __init__(self, width = 1, height = 2):
        self.width = width
        self.height = height
    def getArea(self):
        return self.width * self.height
    def getPerimeter(self):
        return 2*self.width + 2*self.height

# 7.3

class Account:
    def __init__(self, id:int = 0, balance:float = 100, annualInterestRate:float = 0):
        self.id = id
        self.balance = balance
        self.annualInterestRate = annualInterestRate

    def getId(self):
        return self.id

    def setID(self, newID):
        self.id = newID

    def getBalance(self):
        return self.balance

    def setBalance(self, newBalance):
        self.balance = newBalance

    def getAnnualInterestRate(self):
        return self.annualInterestRate

    def setAnnualInterestRate(self, newAnnualInterestRate):
        self.annualInterestRate = newAnnualInterestRate

    def getMonthlyInterest(self):
        monthlyInterest = self.balance * ((self.annualInterestRate / 100) / 12)
        return monthlyInterest
    def withdraw(self, amt):
        self.balance -= amt
    def deposit(self, amt):
        self.balance += amt


# 7.2
import math

class Stock:
    def __init__(self, symbol:str, name: str, previousClosing:float, currentPrice:float):
        self.symbol = symbol
        self.name = name
        self.previousClosing = previousClosing
        self.currentPrice = currentPrice
    def getStockName(self):
        return self.name
    def getStockSymbol(self):
        return self.symbol
    def getStockPreviousPrice(self ):
        return self.previousClosing
    def setStockPreviousPrice(self, price):
        self.previousClosing = price
    def getStockCurrentPrice(self):
        return self.currentPrice
    def setStockCurrentPrice(self, price):
        self.currentPrice = price
    def getChangePercent(self):
        increase = self.currentPrice - self.previousClosing
        percentChange = increase / self.previousClosing * 100
        return percentChange

class QuadratEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def getA(self):
        return self.a
    def getB(self):
        return self.b
    def getB(self):
        return self.b
    def getRoot1(self):
        d = (b ** 2) - (4 * a * c)
        sol2 = (-b+math.sqrt(d))/(2*a)
        if (math.pow(self.b, 2) - 4*self.a * self.b) < 0:
            return 0
        else:
            return sol2
    def getRoot2(self):
        d = (b ** 2) - (4 * a * c)
        sol1 = (-b-math.sqrt(d))/(2*a)
        if (math.pow(self.b, 2) - 4*self.a * self.b) < 0:
            return 0
        else:
            return sol1

class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    def getHour(self):
        return self.hour
    def getMinute(self):
        return self.minute
    def getSecond(self):
        return self.second

    def format(self):
        return "%d:%02d:%02d" % (self.hour, self.minute, self.second)

    def setTime(self, seconds):
        seconds = seconds % (24 * 3600)
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60

        return "%d:%02d:%02d" % (hour, minutes, seconds)


if __name__ == '__main__':
    rectangle1 = Rectangle(4, 40)
    print("Rectangle 1 Area: ", rectangle1.getArea())
    print("Rectangle 1 Perimeter: ", rectangle1.getPerimeter())
    print("Rectangle 1 Width: ", rectangle1.width)
    print("Rectangle 1 Height: ", rectangle1.height)

    print("")
    print("")

    rectangle2 = Rectangle(3.5, 35.7)
    print("Rectangle 2 Area: ", rectangle2.getArea())
    print("Rectangle 2 Perimeter: ", rectangle2.getPerimeter())
    print("Rectangle 2 Width: ", rectangle2.width)
    print("Rectangle 2 Height: ", rectangle2.height)

    print("-------------------------------------------------")
    print("")

    account = Account(5, 50000, 4.5)
    print("Account ID is: ", account.id)
    print("Account Balance is: ", account.balance)
    print("Account Annual Interest Rate is", account.annualInterestRate)
    print("Account Monthly Interest is", account.getMonthlyInterest())
    account.deposit(25000)
    print("Account deposit is $25000. The new account balance is", account.balance)
    account.withdraw(25000)
    print("Account withdrawal is $25000. The new account balance is", account.balance)

    print("")
    print("")
    account.setID(5)
    account.setBalance(75000)
    account.setAnnualInterestRate(5)
    account = Account(5, 50000, 4.5)
    print("New account ID is: ", account.id)
    print("New account Balance is: ", account.balance)
    print("New account Annual Interest Rate is", account.annualInterestRate)
    print("New account Monthly Interest is", account.getMonthlyInterest())
    account.deposit(5000)
    print("Account deposit is $25000. The new account balance is", account.balance)
    account.withdraw(2000)
    print("Account withdrawal is $25000. The new account balance is", account.balance)

    print("----------------------------------------------------------------------------")
    print("")
    print("")

    stock = Stock("INTC", "Intel Corporation", 20.5, 20.25)
    print("The symbol is", stock.getStockSymbol())
    print("The name is", stock.getStockName())
    print("The current Price is", stock.getStockPreviousPrice())
    print("The new price is", stock.getStockCurrentPrice())
    if stock.getChangePercent() < 0:
        print("The percent change is a decrease of", abs(stock.getChangePercent()))
    else:
        print("The percent change is an increase of", stock.getChangePercent())

    print("----------------------------------------------------------------------------")
    print("")
    print("")

    print("Enter a number for a: ", end='')
    a = float(input())
    print("Enter a number for b: ", end='')
    b = float(input())
    print("Enter a number for c: ", end='')
    c = float(input())

    equation = QuadratEquation(a, b, c)
    discrim = (b ** 2) - (4 * a * c)
    if discrim < 0:
        print("The equation doesn't have any roots")
    else:
        print("Root 1 is", equation.getRoot1())
        print("Root 2 is", equation.getRoot2())

print("------------------------------------------------------------------------------------")
print("")
print("")

time = Time(12, 41, 6)
print("The current time is: ", time.format())
print("Enter the elapsed time: ", end= '')
elapsedTime = int(input())
print("The hour:minute:second for the elapsed time is", time.setTime(elapsedTime))
