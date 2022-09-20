s_list = list(map(int, input().split()))
t_list = list(map(int, input().split()))

s = sum(s_list)
t = sum(t_list)

print(max(s,t))