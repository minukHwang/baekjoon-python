tri = []

while True:
    tri = list(map(int,input().split()))
    if sum(tri) == 0:
        break
    elif max(tri) >= sum(tri) - max(tri):
        print("Invalid")
    else:
        if len(set(tri)) == 1:
            print("Equilateral")
        elif len(set(tri)) == 2:
            print("Isosceles")
        elif len(set(tri)) == 3:
            print("Scalene")