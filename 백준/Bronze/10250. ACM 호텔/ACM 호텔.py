n = int(input())
for i in range(n):
    h, w, n = map(int, input().split())
    ho = n // h + 1
    floor = n % h
    if n%h == 0:
        ho -= 1
        floor = h
    print(int(str(floor)+"{0:02d}".format(ho)))