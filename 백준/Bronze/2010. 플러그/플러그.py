import sys

tab = int(sys.stdin.readline())
total_plug = 1

for i in range(tab):
    plug = int(sys.stdin.readline())
    total_plug -= 1
    total_plug += plug

print(total_plug)

