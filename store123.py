import random
class shop:
     a = []
     b = 0
     def abc(self):
          while True:
               print("|---------------------------------|")
               print("|1_calculator price : 7$          |")
               print("|2_pencil price : 1$              |")
               print("|3_pen price : 1$                 |")
               print("|4_markers : 7$                   |")
               print("|5_book price : 7$                |")
               print("|6_ruber + sharpener price : 2$   |")
               print("|7_ruber price : 1.5$             |")
               print("|8_sharpener price : 1.5$         |")
               print("|9_pencil + pen price : 2$        |")
               print("|10_all item price : 25$          |")
               print("|11_exit                          |")
               print("|---------------------------------|")
               p = int(input("enter your choice : "))
               if p==1:
                    n = int(input("how maney calculator do you need : "))
                    m = n * 7
                    print(m)
                    self.a.append(m)
               elif p==2:
                    n = int(input("how maney pencil do you need : "))
                    m = n * 1
                    print(m)
                    self.a.append(m)
               elif p==3:
                    n = int(input("how maney pen do you need : "))
                    m = n * 1
                    print(m)
                    self.a.append(m)
               elif p==4:
                    n = int(input("how maney markers do you need : "))
                    m = n * 7
                    print(m)
                    self.a.append(m)
               elif p==5:
                    n = int(input("how maney book do you need : "))
                    m = n * 7
                    print(m)
                    self.a.append(m)
               elif p==6:
                    n = int(input("how maney ruber + sharpener do you need : "))
                    m = n * 2
                    print(m)
                    self.a.append(m)
               elif p==7:
                    n = int(input("how maney ruber do you need : "))
                    m = n * 1.5
                    print(m)
                    self.a.append(m)
               elif p==8:
                    n = int(input("how maney sharpener do you need : "))
                    m = n * 1.5
                    print(m)
                    self.a.append(m)
               elif p==9:
                    n = int(input("how maney pencil + pen do you need : "))
                    m = n * 2
                    print(m)
                    self.a.append(m)
               elif p==10:
                    n = int(input("how maney all item do you need : "))
                    m = n * 25
                    print(m)
                    self.a.append(m)
               elif p==11:
                    for f in self.a:
                         self.b = self.b + f
                         print(self.b)
               break
abcde = shop()
print("1_go staionary")
print("2_not go staionary")
q = int(input("enter your choice : "))
if q==1:
     while True:
          abcde.abc()

