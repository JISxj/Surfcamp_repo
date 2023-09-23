def max_ind(sp):
    max_ch = max(sp)
    for i in range(len(sp)):
        if max_ch == sp[i]:
            return i


def max_ch(ind_arr):
    maxx = ind_arr[0]
    for i in range(len(ind_arr)):
        if sp[ind_arr[i]] > sp[maxx]:
            maxx = ind_arr[i]
    return maxx


n = int(input())
sp = list(map(int, input().split()))
ind = max_ind(sp)
ind_arr = []
vasiliy_ind = 0
vasiliy_place = 0
for i in range(ind + 1, len(sp) - 1):
    if sp[i] % 10 == 5 and sp[i + 1] < sp[i]:
        ind_arr.append(i)
        vasiliy_place = 1

if vasiliy_place != 0:
    vasiliy_ind = max_ch(ind_arr)
    k = 0
    for meter in sp:
        if meter > sp[vasiliy_ind]:
            k += 1
    print(k + 1)
else:
    print(0)
