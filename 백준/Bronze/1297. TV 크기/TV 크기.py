d,h,w = map(int,input().split())

x = d/((h**2+w**2)**(1/2))

h = int(x*h)
w = int(x*w)

print(h,w)