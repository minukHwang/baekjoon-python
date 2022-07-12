month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
date = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

x, y = map(int, input().split())

day = sum(month[:x-1]) + y

print(date[day%7])