customers = dict()
st = input().split()
while st:
    if st[0] in customers:
        dict_of_goods = customers[st[0]]
        if st[1] in dict_of_goods:
            dict_of_goods[st[1]] += int(st[2])
        else:
            dict_of_goods[st[1]] = int(st[2])
    else:
        customers[st[0]] = {st[1]: int(st[2])}
    st = input().split()

customers = list(sorted(customers.items()))
for string in customers:
    print(string[0] + ":")
    list_of_goods = list(sorted(string[1].items()))
    for good in list_of_goods:
        print(good[0], good[1])

