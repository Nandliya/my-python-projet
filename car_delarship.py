class car_delarship:
    b = []
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
    def total(self):
        buy = 0
        total = 10000
        for bay in self.b:
            buy = buy + bay
        total = total + buy
        print("with out gst bill : ", buy)
        print("with gst bill : ", total)
cars = car_delarship()
while True:
    print("1_get a car")
    print("2_not a car")
    c  = int(input("enter your choice"))
    if c==1:
        cars.hyundai()
    elif c==2:
        cars.total()
        breaks
