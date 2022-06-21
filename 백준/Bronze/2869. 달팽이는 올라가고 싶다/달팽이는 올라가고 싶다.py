import math

a, b, v = map(int, input().split())
min_v = v - a
day = math.ceil(min_v / (a-b)) + 1

print(day)