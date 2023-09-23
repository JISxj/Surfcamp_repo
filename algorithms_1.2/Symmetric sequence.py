def is_tail(st):
    for i in range(len(st) - 1, -2, -1):
        if st[i] == st[i - 1]:
            return True
        elif st[i] != st[i - 1]:
            return False
    return False


def remove_tail(st):
    ans = st[:]
    for i in range(len(st) - 1, -2, -1):
        if st[i] == st[i - 1]:
            ans = "".join([ans[x] for x in range(len(ans)) if x != i])
            ans = "".join([ans[x] for x in range(len(ans)) if x != i - 1])
        elif st[i] != st[i - 1]:
            return ans
    return ans


def symmetric(sequence):
    if sequence[::-1] == sequence:
        return True
    return False


def mirror(sequence, point):
    left = sequence[:point]
    right = sequence[:point][::-1]
    return left + sequence[point] + right


def shadow_mirror(sequence, point):
    side = sequence[:point] + sequence[point]
    return side + side[::-1]


def func(sequence):
    huge_arr = []
    if symmetric(sequence):
        return 0
    tail_checker = is_tail(sequence)
    sequence = remove_tail(sequence)
    if tail_checker:
        mirror_sequence = sequence[::-1]
        return len(sequence), [x for x in mirror_sequence]
    mirror_point = len(sequence) // 2
    for i in range(mirror_point,len(sequence)):
        currsequence = mirror(sequence, i)
        shadowsequence = "-1"
        if i != len(sequence) - 1:
            shadowsequence = shadow_mirror(sequence, i)
        if sequence in currsequence:
            result = currsequence[len(sequence):]
            huge_arr.append((len(result), [x for x in result]))
        if sequence in shadowsequence:
            result = shadowsequence[len(sequence):]
            huge_arr.append((len(result), [x for x in result]))
    return min(huge_arr)


n = int(input())
sequence = "".join(input().split())
res = func(sequence)
if res == 0:
    print(0)
else:
    print(res[0])
    print(*res[1])

