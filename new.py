class clc:
    def add(self):
        a = int(input("enter your add cohise : "))
        b = int(input("enter your add cohise : "))
        c = a + b
        print(c)
    def subtract(self):
        a = int(input("enter your add cohic : "))
        b = int(input("enter your add cohic : "))
        c = a - b
        print(c)
    def multiply(self):
        a = int(input("enter your add cohic : "))
        b = int(input("enter your add cohic : "))
        c = a * b
        print(c)
    def divide(self):
        a = int(input("enter your add cohic : "))
        b = int(input("enter your add cohic : "))
        c = a / b
        print(c)
c=clc()
while True:
    print("1.add")
    print("2.subtract")
    print("3.multiply")
    print("4.divide")
    print("5.exit")
    g = int(input("enter your cohic : "))
    if g==1:
        c.add()
    elif g==2:
        c.subtract()
    elif g==3:
        c.multiply()
    elif g==4:
        c.divide()
    else:
        break