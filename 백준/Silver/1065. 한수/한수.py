n = int(input())
han = list()

def differ(num):
    num = str(num)
    differences = set()
    if len(num) == 1:
        differences = 1
    else:
        for i in range(1,len(num)):
            differences.add(int(num[i]) - int(num[i-1]))
        differences = len(differences)

    return differences

for i in range(1,n+1):
    d = differ(i)
    if d == 1:
        han.append(i)

print(len(han))