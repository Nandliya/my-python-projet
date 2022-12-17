class home:
    re = []
    de = []
    def buy_home(self):
                print("1 bhk", "2 bhk", "3 bhk")
                print("$1000", "2000$", "3000$")
                bh = int(input("enter you choice : "))
                if bh==1:
                    hm = int(input("how many property do you want"))
                    ph = hm*1000
                    self.de.append(ph)
                elif bh==2:
                    hm = int(input("how many property do you want"))
                    ph = hm*2000
                    self.de.append(ph)
                elif bh==3:
                    hm = int(input("how many property do you want"))
                    ph = hm*3000
                    self.de.append(ph)
    def buy_rent(self):
                print("1 bhk", "2 bhk", "3 bhk")
                print("$100", "200$", "300$")
                bh = int(input("enter your choice"))
                if bh==1:
                    hm = int(input("how many rent property do you want"))
                    rh = hm*100
                    self.re.append(rh)
                elif bh==2:
                    hm = int(input("how many rent property do you want"))
                    rh = hm*200
                    self.re.append(rh)
                elif bh==3:
                    hm = int(input("how many rent property do you want"))
                    rh = hm*300
                    self.re.append(rh)            
    def totle(self):
        rent = 0 
        home = 0
        t = 0
        for r in self.re:
            rent = rent + r
        for p in self.de:
            home = home + p
        t = t + rent + home
        print("rent bill : ", rent)
        print("home bill : ", home)
        print("total bill : ", t)
        
        
        
        
        
hom = home()
while True:
    print("1_buy home : ")
    print("2_buy home in a rent : ")
    print("3_total")
    h = int(input("enter your choice"))
    if h==1:
        hom.buy_home()
    elif h==2 :
        hom.buy_rent()
    elif h==3:
        hom.totle()
