for i in range(3):
    yoot = list(map(int, input().split()))
    total = sum(yoot)

    if total == 4:
        print("E")
    elif total == 3:
        print("A")
    elif total == 2:
        print("B")
    elif total == 1:
        print("C")
    elif total == 0:
        print("D")