n = int(input())
for item in range(n):
    a = list(map(int, input().split()))
    students = a[0]
    del a[0]
    total = 0
    count = 0

    for item in a:
        total += item

    for item in a:
        if item > total / students:
            count += 1

    print('{:.3f}%'.format(count/students*100))