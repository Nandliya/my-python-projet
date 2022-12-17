class cube_shop:
     An = []
     sc = []
     nc = []
     Ass = []
     am = []
     def cube(self):
          while True:
               print("|-----------------------------|")
               print("|  1_Twisted Cube : 10$       |")
               print("|  2_Mirror Cube : 15$        |")
               print("|  3_Mastermorphix Cube : 10$ |")
               print("|  4_Cubelelo Cube : 10$      |")
               print("|  5_Lemon Cube : 10$         |")
               print("|  6_2x2 Cube : 10$           |")
               print("|  7_3x3 Cube : 10$           |")
               print("|  8_4x4 Cube : 10$           |")
               print("|  9_5x5 Cube : 10$           |")
               print("|  10_6x6 Cube : 10$          |")
               print("|  11_bill                    |")
               print("|-----------------------------|")
               a = int(input("enter your choice : "))
               if a==1:
                    n = int(input("how maney Twisted Cube you need"))
                    m = n * 10
                    self.sc.append(n)
                    self.Ass.append(m)
               elif a==2:
                    n = int(input("how maney Mirror Cube you need"))
                    m = n * 15
                    self.sc.append(n)
                    self.Ass.append(m)
               elif a==3:
                    n = int(input("how maney Mastermorphix Cube Cube you need"))
                    m = n * 10
                    self.sc.append(n)
                    self.Ass.append(m)
               elif a==4:
                    n = int(input("how maney Cubelelo Cube you need"))
                    m = n * 10
                    self.sc.append(n)
                    self.Ass.append(m)
               elif a==5:
                    n = int(input("how maney Lemon Cube you need"))
                    m = n * 10
                    self.sc.append(n)
                    self.Ass.append(m)
               elif a==6:
                    n = int(input("how maney 2x2 Cube you need"))
                    m = n * 10
                    self.nc.append(n)
                    self.An.append(m)
               elif a==7:
                    n = int(input("how maney 3x3 Cube you need"))
                    m = n * 10
                    self.nc.append(n)
                    self.An.append(m)
               elif a==8:
                    n = int(input("how maney 4x4 Cube Cube you need"))
                    m = n * 10
                    self.nc.append(n)
                    self.An.append(m)
               elif a==9:
                    n = int(input("how maney 5x5 Cube you need"))
                    m = n * 10
                    self.nc.append(n)
                    self.An.append(m)
               elif a==10:
                    n = int(input("how maney 6x6 Cube you need"))
                    m = n * 10
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
                    print("normel cube : ",normel)
                    print("normel cube money : ",an)
                    print("shaip shift cube : ",shape)
                    print("shaip shift cube money : ",ass)
                    print("all cube : ",al)
                    print("all cube money : ",money)
                    break
rs = cube_shop()
print("1_go cube shop")
print("2_not go cube shop")
abc = int(input("enter your choice : "))
if abc==1:
     rs.cube()      