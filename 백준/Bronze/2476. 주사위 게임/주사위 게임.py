n = int(input())
result = []

for i in range(n):
    a, b, c = map(int, input().split())
    max_num = max([a,b,c])
    if a == b and b == c :
        result.append(10000 + a*1000)
    elif a == b or b == c or a == c:
        if a == b:
            result.append(1000 + a*100)
        elif b == c:
            result.append(1000 + b*100)
        else:
            result.append(1000 + c*100)
    else:
        result.append(max_num * 100)

print(max(result))
    