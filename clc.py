while True:
    print("1.add")
    print("2.subtract")
    print("3.multiply")
    print("4.divide")
    print("5.exit")
    c = int(input("enter your cohise"))
    if c == 1 :
        a = int(input("enter your cohic"))
        b = int(input("enter your cohic"))
        c = a+b
        print(c)
    elif c==2 :
        a = int(input("enter your cohic"))
        b = int(input("enter your cohic"))
        d = a-b
        print(d)
    elif c==3 :
         a = int(input("enter your cohic"))
         b = int(input("enter your cohic"))
         e = a*b
         print(e)
    elif c==4 :
         a = int(input("enter your cohic"))
         b = int(input("enter your cohic"))
         f = a/b
         print(f)
    elif c==5 :
        break