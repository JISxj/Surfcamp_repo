n = int(input())
arr = sorted(list(map(int, input().split())))
ch = int(input())

right = len(arr) - 1
left = 0
while left != right:
    middle = (right + left) // 2
    if (abs(right - left) == 1 or abs(right - left) == 2) and ch != arr[middle]:
        middle = (right + left) // 2
        if ch > arr[middle]:
            print(arr[middle + 1])
        elif ch < arr[middle]:
            print(arr[(right + left - 1) // 2])
        break
    if ch > arr[middle]:
        left = middle + 1
    elif ch < arr[middle]:
        right = middle - 1
    else:
        print(arr[middle])
        break
if len(arr) == 1:
    print(arr[0])

