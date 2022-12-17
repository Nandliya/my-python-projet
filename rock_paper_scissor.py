import random

while True:
    print("1.rock")
    print("2.paper")
    print("3.scissor")
    p = int(input("enier your choice"))
    r = random.randint(1, 3)
    if p==r:
        print(r)
        print("Tie")
    elif p<r:
        print(r)
        print("you are loose")
    elif p>r:
        print(r)
        print("you are winner")
    else:
        print("your are chiting")
        break
    