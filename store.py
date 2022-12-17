class store:
       fruit_bill = []
       chips_bill = []
       veglable_bill = []
       b = []
       def fruit(self):
              print("1_per kg 3$_apple")
              print("2_per kg 5$_mango")
              print("3_per kg 2$_banana")
              print("4_per kg 9$_pinapple")
              print("5_per kg 10$_grapes")
              f = int(input("enter your cohic : "))
              if f==1:
                     fs=int(input("enter your apple kg : "))
                     fp = fs*3
                     self.fruit_bill.append(fp)
              elif f==2:
                     fs=int(input("enter your mango kg : "))
                     fp = fs*5
                     self.fruit_bill.append(fp)
              elif f==3:
                     fs=int(input("enter your banana kg : "))
                     fp = fs*2
                     self.fruit_bill.append(fp)
              elif f==4:
                     fs=int(input("enter your pinapple kg : "))
                     fp = fs*9
                     self.fruit_bill.append(fp)
              else:
                     fs=int(input("enter your grapes kg : "))
                     fp = fs*10
                     self.fruit_bill.append(fp)
       def veglable(self):
              print("1_per kg 1$_chil")
              print("2_per kg 3$_tamato")
              print("3_per kg 5$_patato")
              print("4_per kg 3$_chabage")
              print("5_per kg 7$_bnees")
              v = int(input("enter your cohic : "))
              if v==1:
                     vs=int(input("enter your chil kg : "))
                     vp = vs*1
                     self.veglable_bill.append(vp)
              elif v==2:
                     vs=int(input("enter your tamato kg : "))
                     vp = vs*3
                     self.veglable_bill.append(vp)
              elif v==3:
                     vs=int(input("enter your patato kg : "))
                     vp = vs*5
                     self.veglable_bill.append(vp)
              elif v==4:
                     vs=int(input("enter your chabage kg : "))
                     vp = vs*3
                     self.veglable_bill.append(vp)
              else:
                     vs=int(input("enter your bnees kg :"))
                     vp = vs*7
                     self.veglable_bill.append(vp)
       def chips(self):
              print("1_per kg 1$_pringles")
              print("2_per kg 1$_too yumm")
              print("3_per kg 1$_bingo")
              print("4_per kg 1$_lays")
              print("5_per kg 1$_doritos")
              c = int(input("enter your cohic : "))
              if c==1:
                     cs=int(input("enter your pringles : "))
                     cp = cs*1
                     self.chips_bill.append(cp)
              elif c==2:
                     cs=int(input("enter your too yumm : "))
                     cp = cs*1
                     self.chips_bill.append(cp)
              elif c==3:
                     cs=int(input("enter your bingo : "))
                     cp = cs*1
                     self.chips_bill.append(cp)
              elif c==4:
                     cs=int(input("enter your lays : "))
                     cp = cs*1
                     self.chips_bill.append(cp)
              else:
                     cs=int(input("enter your doritos :"))
                     cp = cs*1
                     self.chips_bill.append(cp)
       def hyundai(self):
          print("1_creta : 11.5 lack")
          print("2_sonata : 5.75 lack")
          print("3_i10 : 4.3 lack")
          print("4_i20 : 7.5 lack")
          print("5_santro : 4.39 lack")
          b = int(input("enter your choice"))
          if b==1:
              bu = int(input("how many cars do you need : "))
              by = bu*1150000
              self.b.append(by)
          elif b==2:
              bu = int(input("how many cars do you need : "))
              by = bu*575000
              self.b.append(by)
          elif b==3:
              bu = int(input("how many cars do you need : "))
              by = bu*430000
              self.b.append(by)
          elif b==4:
              bu = int(input("how many cars do you need : "))
              by = bu*750000
              self.b.append(by)
          elif b==5:
              bu = int(input("how many cars do you need : "))
              by = bu*439000
              self.b.append(by)
       def totalbill(self):
              self.fruitstotal = 0
              self.vegitabletotal = 0
              self.chipstotal = 0
              buy = 0
              for bay in self.b:
                    buy = buy + bay
              for f in self.fruit_bill:
                     self.fruitstotal = self.fruitstotal+f

              for f in self.veglable_bill:
                     self.vegitabletotal = self.vegitabletotal+f

              for f in self.chips_bill:
                     self.chipstotal = self.chipstotal+f
              
              self.finalbill = self.fruitstotal + self.vegitabletotal + self.chipstotal + buy
              print("Fruits bill total : ",self.fruitstotal )
              print("Vigitables bill total : ", self.vegitabletotal)
              print("Chips bill total : ",self.chipstotal )
              print("Car bill total : ",buy )
              print("Final bill total : ",self.finalbill )

sto = store()
print("1.go to store")
print("2.exit")

c = int(input("enter your choice : "))
if c==1:
       while True:
              print("1.fruit")
              print("2.vegtable")
              print("3.chips")
              print("4.buy a car")
              print("5.exit")
              s = int(input("enter your choice : "))
              if s==1:
                     sto.fruit()
              elif s==2:
                     sto.veglable()
              elif s==3:
                     sto.chips()
              elif s==4:
                     sto.hyundai()
              elif s==5:
                     sto.totalbill()
                     break
              else:
                     print("Wrong choice ")