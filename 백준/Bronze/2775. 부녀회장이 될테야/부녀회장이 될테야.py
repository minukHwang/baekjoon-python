n = int(input())

for i in range(n):
    k = int(input())
    n = int(input())
    floor = [i for i in range(1,n+1)]
    next_floor = [0]*n
    
    for j in range(k):
        for i in range(len(floor)):
            next_floor[i] = sum(floor[:i+1])
        floor = next_floor.copy()
    
    print(next_floor[n-1])