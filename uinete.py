class cube_shop:
     An = []
     sc = []
     nc = []
     Ass = []
     am = []
     def cube(self):
          while True:
               print("|-----------------------------|")
               print("|  1_tubelight                |")
               print("|  2_fridge / freezer         |")
               print("|  3_32 inch led tv           |")
               print("|  4_bulb                     |")
               print("|  5_Extractor Fan            |")
               print("|  6_ac                       |")
               print("|  7_washing machine          |")
               print("|  8_phone                    |")
               print("|  9_gayser                   |")
               print("|  10_laptop computer         |")
               print("|  11_light bill              |")
               print("|-----------------------------|")
               a = int(input("enter your choice : "))
               if a==1:
                    n = int(input("how maney Tubelight in your home"))
                    a = int(input("how maney hour on Tubelight in your home"))
                    m = n *a* 100
                    print("unit : ",m)
                    self.sc.append(n)
                    self.Ass.append(m)
               elif a==2:
                    n = int(input("how maney fridge / freezer in your home"))
                    a = int(input("how maney hour on fridge / freezer in your home"))
                    m = n *a* 400
                    print("unit : ",m)
                    self.sc.append(n)
                    self.Ass.append(m)
               elif a==3:
                    n = int(input("how maney 32 inch led tv in your home"))
                    a = int(input("how maney hour on 32 inch led tv in your home"))
                    m = n *a* 60
                    print("unit : ",m)
                    self.sc.append(n)
                    self.Ass.append(m)
               elif a==4:
                    n = int(input("how maney bulb in your home"))
                    a = int(input("how maney hour on bulb in your home"))
                    m = n *a* 100
                    print("unit : ",m)
                    self.sc.append(n)
                    self.Ass.append(m)
               elif a==5:
                    n = int(input("how maney Extractor Fan in your home"))
                    a = int(input("how maney hour on Extractor Fan in your home"))
                    m = n *a* 12
                    print("unit : ",m)
                    self.sc.append(n)
                    self.Ass.append(m)
               elif a==6:
                    n = int(input("how maney ac in your home"))
                    a = int(input("how maney hour on ac in your home"))
                    m = n *a* 80
                    print("unit : ",m)
                    self.nc.append(n)
                    self.An.append(m)
               elif a==7:
                    n = int(input("how maney washing machine in your home"))
                    a = int(input("how maney hour on washing machine in your home"))
                    m = n *a* 500
                    print("unit : ",m)
                    self.nc.append(n)
                    self.An.append(m)
               elif a==8:
                    n = int(input("how maney phone in your home"))
                    a = int(input("how maney hour on phone in your home"))
                    m = n *a* 7
                    print("unit : ",m)
                    self.nc.append(n)
                    self.An.append(m)
               elif a==9:
                    n = int(input("how maney gayser in your home"))
                    a = int(input("how maney hour on gayser in your home"))
                    m = n *a* 2
                    print("unit : ",m)
                    self.nc.append(n)
                    self.An.append(m)
               elif a==10:
                    n = int(input("how maney laptop computer in your home"))
                    a = int(input("how maney hour on laptop computer in your home"))
                    m = n *a* 100
                    print("unit : ",m)
                    self.nc.append(n)
                    self.An.append(m)
               elif a==11:
                    normel = 0
                    shape = 0
                    money = 0
                    an = 0
                    ass = 0
                    al = 0
                    for nor in self.nc:
                         normel = normel + nor
                    for sp in self.sc:
                         shape = shape + sp
                    for a_n in self.An:
                         an = an + a_n
                    for a_s in self.Ass:
                         ass = ass + a_s
                    al = al + shape + normel
                    money = money + an + ass
                    print("light unit bill : ",money)
                    if money >= 1000:
                         money = money * 0.007
                         print("light money bill : ",money)
                    break
rs = cube_shop()
print("1_go light bill  shop")
print("2_not go light shop")
abc = int(input("enter your choice : "))
if abc==1:
     rs.cube()      