class hotle:
    room_bill = []
    food_bill = []
    laundry_bill = []
    def room(self):
        print("1_normol room : 1000")
        print("2_ac room : 3000")
        print("3_ac window room : 5000")
        r = int(input("enter your room : "))
        if r==1:
            rs = int(input("enter you need room : "))
            rp = rs*1000
            self.room_bill.append(rp)
        elif r==2:
            rs = int(input("enter you need room : "))
            rp = rs*3000
            self.room_bill.append(rp)
        else:
            rs = int(input("enter you need room : "))
            rp = rs*5000
            self.room_bill.append(rp)
    def food(self):
        while True:
            print("1_lunch : 100")
            print("2_dinner : 200")
            print("3_cofe : 10")
            print("4_Tea : 15")
            print("5_bicket : 10 20 30 ")
            print("6_exit")
            f = int(input("enter your food : "))
            if f==1:
                n = int(input("you need lunch?? : "))
                nr = n*100
                self.food_bill.append(nr)
            elif f==2:
                n = int(input("you need dinner?? : "))
                nr = n*200
                self.food_bill.append(nr)
            elif f==3:
                n = int(input("you need cofe?? : "))
                nr = n*10
                self.food_bill.append(nr)
            elif f==4:
                n = int(input("you need tea?? : "))
                nr = n*15
                self.food_bill.append(nr)
            elif f==5:
                print("1_normel bicket : 5")
                print("2_crem bicket : 10")
                print("3_big crem packet bicket : 20")
                b = int(input("enter your choice : "))
                if b==1:
                    n = int(input("normel bicket?? : "))
                    nr = n*5
                    self.food_bill.append(nr)
                elif b==2:
                    n = int(input("crem bicket?? : "))
                    nr = n*10
                    self.food_bill.append(nr)
                elif b==3:
                    n = int(input("big crem packet bicket?? : "))
                    nr = n*20
                    self.food_bill.append(nr)
            else:
                break
    def laundry (self):
        while True:
            print("1_shart : 5")
            print("2_tshart : 5")
            print("3_jeans : 6")
            print("4_pant : 6")
            print("5_blazer : 10")
            print("6_exit")
            l = int(input("enter your choice : "))
            if l==1:
                w = int(input("enter your wash shart : ")) 
                wp = w*5
                self.laundry_bill.append(wp)
            elif l==2:
                w = int(input("enter your wash tshart : ")) 
                wp = w*5
                self.laundry_bill.append(wp)
            elif l==3:
                w = int(input("enter your wash jeans : ")) 
                wp = w*6
                self.laundry_bill.append(wp)
            elif l==4:
                w = int(input("enter your wash pant : ")) 
                wp = w*6
                self.laundry_bill.append(wp)
            elif l==5:
                w = int(input("enter your wash blazer : ")) 
                wp = w*10
                self.laundry_bill.append(wp)
            elif l==6:
                break
    def totle(self):
                self.room_total = 0
                self.food_total = 0
                self.laundry_total = 0
                self.totle_bill = 0
                for t in self.room_bill:
                                self.room_total = self.room_total+t
                for t in self.food_bill:
                                self.food_total = self.food_total+t
                for t in self.laundry_bill:
                                self.laundry_total = self.laundry_total+t
                self.totle_bill = self.room_total + self.food_total + self.laundry_total 
                print("room bill total : ",self.room_total )
                print("food bill total : ", self.food_total)
                print("laundre bill total : ",self.laundry_total )
                print("Final bill total : ",self.totle_bill)
hot=hotle()
print("1_go hotel")    
print("2_exit")
h = int(input("enter your cohice : "))
if h==1:
    print("thanks_for_comeing")
    while True:
        print("1_buy_room")
        print("2_buy_food")
        print("3_laundry")
        print("4_exit")
        hm = int(input("enter your cohice : "))
        if hm==1:
            hot.room()
        elif hm==2:
            hot.food()
        elif hm==3:
            hot.laundry()
        else:
            hot.totle()
            break