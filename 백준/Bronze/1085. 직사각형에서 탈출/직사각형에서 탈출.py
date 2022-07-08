x,y,w,h = map(int, input().split())
min_length = [x,y,w-x,h-y]

print(min(min_length)) 