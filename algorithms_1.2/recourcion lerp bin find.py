def bin_find(arr, left, right, ch):
    if len(arr) == 1:
        return arr[0]
    if left == right:
        return arr[left]
    middle = (left + right) // 2
    if ch > arr[middle]:
        left = middle + 1
        if left >= len(arr):
            left = len(arr) - 1
        return bin_find(arr, left, right, ch)
    elif ch < arr[middle]:
        right = middle - 1
        if right < 0:
            right = 0
        return bin_find(arr, left, right, ch)
    else:
        return arr[middle]


n = int(input())
arr = sorted(list(map(int, input().split())))
ch = int(input())
res = bin_find(arr, 0, len(arr) - 1, ch)
print(res)
