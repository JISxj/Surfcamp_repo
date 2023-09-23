def extend(top_left, top_right, bot_right, bot_left, t):
    return top_left + t, top_right + t, bot_right - t, bot_left - t


def intersect(borders1, borders2):
    return [min(borders1[0], borders2[0]), min(borders1[1], borders2[1]),
            max(borders1[2], borders2[2]), max(borders1[3], borders2[3])]


t, d, n = map(int, input().split())
posRect = (0, 0, 0, 0)
for _ in range(n):
    posRect = extend(*posRect, t)
    target_x, target_y = map(int, input().split())
    targetRect = extend(target_x - target_y, target_x + target_y, target_x - target_y, target_x + target_y, d)
    posRect = intersect(posRect, targetRect)

ans = []
for posDiagonal in range(posRect[2], posRect[0] + 1):
    for negDiagonal in range(posRect[3], posRect[1] + 1):
        if (posDiagonal + negDiagonal) % 2 == 0:
            x = (posDiagonal + negDiagonal) // 2
            y = negDiagonal - x
            ans.append((x, y))
print(len(ans))
for _ in ans:
    print(*_)

