n = int(input())

for i in range(n):
    num, letter = input().split()
    num = int(num)
    for item in letter:
        for i in range(num):
            print(item, end="")
    print()