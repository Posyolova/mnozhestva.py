n = [int(s) for s in input().split()] # Разбиваем ввод на список чисел
q = set() # для хранения чисел
for num in n:
    if num in q:
        print('YESS') #если число встречалось ранее
    else:
        print('NOOO') # если не встечалось
        q.add(num)
