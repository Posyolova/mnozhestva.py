n = [int(s) for s in input().split()]
q = set()
for num in n:
    if num in q:
        print('YESS')
    else:
        print('NOOO')
        q.add(num)
