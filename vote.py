class vote:
    a = []
    b = []
    c = []
    d = []
    pas = []
    def vote_(self):
        print("press 1 for voteing")
        print("press 3 to exit")
        c = int(input("enter your choice"))
        if c==1:
            while True:
                print("1_player 1 a")
                print("2_player 2 b")
                print("3_player 3 c")
                print("4_player 4 d")
                print("5_result")
                v = int(input("enter your vote"))
                if v==1:
                    self.a.append(1)
                elif v==2:
                    self.b.append(1)
                elif v==3:
                    self.c.append(1)
                elif v==4:
                    self.d.append(1)
                elif v==5:
                    A = 0
                    B = 0
                    C = 0
                    D = 0
                    t = 0
                    for va in self.a:
                        A = A+va
                    for vb in self.b:
                        B = B+va
                    for vc in self.c:
                        C = C+va
                    for vd in self.d:
                        D = D+va
                    t = t + A + B + C + D
                    lpp = int(input("enter your password"))
                    self.pas.append(lpp)
                    lp = int(input("enter your login password"))
                    for i in self.pas:
                        if i==lp:
                            print("total vote a", A)
                            print("total vote b", B)
                            print("total vote c", C)
                            print("total vote d", D)
                            print("total vote", t)
                            break
vot = vote()
vot.vote_()