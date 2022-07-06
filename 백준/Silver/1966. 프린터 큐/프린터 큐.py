a = int(input())

for i in range(a):
    n, m = map(int, input().split())
    im = list(map(int, input().split()))
    what = [False]*n
    what[m] = True
    count = 0
    
    while len(im) != 0:
        if im[0] == max(im):
            del im[0]
            count += 1
        else:
            im.append(im[0])
            del im[0]
            what.append(what[count])
            del what[count]
            
    print(what.index(True) + 1)