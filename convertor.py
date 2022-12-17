class convertor:
    km_mi = []
    li_ou = []
    sqm_yd = []
    kg_po = []
    c_f = []
    def km_to_mi(self):
        kmi = int(input("enter your kilomiter to mile : "))
        mi = kmi*0.621
        self.km_mi.append(mi)

    def li_to_uo(self):
        kmi = int(input("enter your liter to ounce : "))
        mi = kmi*33.814
        self.li_ou.append(mi)

    def sqm_to_yd(self):
        kmi = int(input("enter your sqmt to yard : "))
        mi = kmi*1.195
        self.sqm_yd.append(mi)

    def kg_to_po(self):
        kmi = int(input("enter your kilogram to pound : "))
        mi = kmi*2.204
        self.kg_po.append(mi)

    def c_to_f(self):
        kmi = int(input("enter your c. to f : "))
        mi = kmi*1.8
        self.c_f.append(mi)

    def total(self):
        k_m_ = 0
        l_o_ = 0
        s_y_ = 0
        k_p_ = 0
        c_f_ = 0
        for km in self.km_mi:
            k_m_ = k_m_ + km
        for lo in self.li_ou:
            l_o_ = l_o_ + lo
        for sy in self.sqm_yd:
            s_y_ = s_y_ + sy
        for kp in self.kg_po:
            k_p_ = k_p_ + kp
        for cf in self.c_f:
            c_f_ = c_f_ + cf + 32
        print("kilo_miter : ", k_m_)
        print("liter_pounc : ", l_o_)
        print("sqmi_yard : ", s_y_)
        print("kilo_pounc : ", k_p_)
        print("c_f : ", c_f_)

col = convertor()
while True:
    print("1_km_to_mi")
    print("2_kg_to_po")
    print("3_sqm_to_yd")
    print("4_li_to_uo")
    print("5_c_to_f")
    print("6_converts")
    c = int(input("enter your choice : "))
    if c==1:
        col.km_to_mi()
    elif c==2:
        col.kg_to_po()
    elif c==3:
        col.sqm_to_yd()
    elif c==4:
        col.li_to_uo()
    elif c==5:
        col.c_to_f()
    else:
        col.total()
        break