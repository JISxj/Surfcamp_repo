n = int(input())
arr = [(float(input()), "")]
for i in range(n - 1):
    st = input().split()
    arr.append((float(st[0]), st[1]))

left = []
right = []
for i in range(n - 1):
    x1 = arr[i][0]
    x2 = arr[i + 1][0]
    distance = arr[i + 1][1]
    interval = (x1 + x2) / 2

    if abs(x1 - x2) < 10 ** (-6):
        continue
    if x1 == x2:
        pass
    else:
        if x1 > x2:
            if distance == "further":
                right.append(interval)
            else:
                left.append(interval)
        else:
            if distance == "further":
                left.append(interval)
            else:
                right.append(interval)


if not right and not left:
    print(*(30.0, 4000.0))
elif right and left:
    print(*(min(min(left), max(right)), max(min(left), max(right))))
elif not right:
    print(*(30.0, min(left)))
else:
    print(*(max(right), 4000.0))


