n = int(input())
for item in range(n):
    a = input()
    total_point = 0
    point = 0
    for i in range(len(a)):
        if a[i] == "O":
            point += 1
        else:
            point = 0
        total_point += point
    print(total_point)