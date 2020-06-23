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
    account.deposit(25000)
    print("Account deposit is $25000. The new account balance is", account.balance)
    account.withdraw(25000)
    print("Account withdrawal is $25000. The new account balance is", account.balance)