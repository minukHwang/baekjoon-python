import sys

count = int(input())

for i in range(count):
    a,b = map(int, input().split())
    print("Case #{0}:".format(i+1), a+b)