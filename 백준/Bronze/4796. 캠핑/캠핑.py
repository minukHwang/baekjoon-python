case = 1

while True:
    l,p,v = map(int, input().split())
    if l + p + v == 0:
        break
    days = (v // p)*l + (v%p if v%p<l else l)
    print("Case {case}: {days}".format(case=case, days=days))
    case += 1