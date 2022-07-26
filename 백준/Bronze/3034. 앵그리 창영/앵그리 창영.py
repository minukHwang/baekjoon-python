n, w, h = map(int, input().split())

max_length = w**2 + h**2

for i in range(n):
    a = int(input())
    if a**2 <= max_length:
        print("DA")
    else:
        print("NE")