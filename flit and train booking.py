class air_plain:
     def plain(self):
          print("1_india to brazil : 1000$")
          print("2_brazil to india : 1000$")
          print("3_india to france : 2000$")
          print("4_france to india : 2000$")
          a = int(input("enter your choice : "))
          if a==1:
               import random
               n = input("enter your name : ")
               print("your ticket book ",n)
               print("plain no. : ", random.randint(1, 100))
               print("seat no. : ", random.randint(1, 100))
          elif a==2:
               import random
               n = input("enter your name : ")
               print("your ticket book ",n)
               print("plain no. : ", random.randint(1, 100))
               print("seat no. : ", random.randint(1, 100))
          elif a==3:
               import random
               n = input("enter your name : ")
               print("your ticket book ",n)
               print("plain no. : ", random.randint(1, 100))
               print("seat no. : ", random.randint(1, 100))
          elif a==4:
               import random
               n = input("enter your name : ")
               print("your ticket book ",n)
               print("plain no. : ", random.randint(1, 100))
               print("seat no. : ", random.randint(1, 100))
class train:
     def train(self):
          print("1_mumbai to jaipur : 500")
          print("2_jaipur to mumbai : 1000")
          print("3_nagpur to mumbai : 600")
          print("4_nagpur to jaipur : 900")
          a = int(input("enter your choice : "))
          if a==1:
               import random
               n = input("enter your name : ")
               print("your ticket book ",n)
               print("train no. : ", random.randint(1, 10000))
               print("seat no. : ", random.randint(1, 10000))
          elif a==2:
               import random
               n = input("enter your name : ")
               print("your ticket book ",n)
               print("train no. : ", random.randint(1, 10000))
               print("seat no. : ", random.randint(1, 10000))
          elif a==3:
               import random
               n = input("enter your name : ")
               print("your ticket book ",n)
               print("train no. : ", random.randint(1, 10000))
               print("seat no. : ", random.randint(1, 10000))
          elif a==4:
               import random
               n = input("enter your name : ")
               print("your ticket book ",n)
               print("train no. : ", random.randint(1, 10000))
               print("seat no. : ", random.randint(1, 10000))
t  = train()
a = air_plain()
while True:
     print("1_plain ticket book")
     print("2_train ticket book")
     c  = int(input("enter your choice : "))
     if c==1:
          a.plain()
     elif c==2:
          t.train()
     else:
          print("Wrong choice")