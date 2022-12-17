import random
class lottry:
     def lottry(self):

          i = 0
          while i!=3:
               print("chance : ",i)
               b = random.randint(1, 10)
               print("1_random lottry number")
               print("2_your favereta lottry number")
               a = int(input("enter your choice : "))
               if a==1:
                    c = random.randint(1, 10)
                    print(c)
                    if c==b:
                         print("your are winer")
                         print("your number : ",c)
                         print("lottry number : ",b)
                         i = i +1
                    elif c!=b:
                         print("your are loss better of luck next time")
                         print("your number : ",c)
                         print("lottry number : ",b)
                         i = i +1
               elif a==2:
                    d = int(input("enetr your number 1 to 10 : "))
                    if d==b:
                         print("your are winer")
                         print("your number : ",d)
                         print("lottry number : ",b)
                         i = i +1
                    elif d!=b:
                         print("your are loss better of luck next time")
                         print("your number : ",d)
                         print("lottry number : ",b)
                         i = i +1 

l = lottry()
print("1_play lottry game")
print("2_not play lottry")
abc = int(input("enter your choice : "))
if abc==1:
     l.lottry()


