def cut_points(x, y, d, mapp):
    points = []
    for coord in mapp:
        if manheten_length(*coord, x, y) <= d:
            points.append(coord)
    return points


def manheten_length(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def generate_path(x, y, t, mapp, target_pos):
    s = []
    new_points = []
    if t == 0:
        return list(set(mapp + [(0, 0)]))
    p1 = (x + 1, y)
    if manheten_length(*p1, *target_pos) <= d + 2:
        new_points.append((x + 1, y))
    p2 = (x - 1, y)
    if manheten_length(*p2, *target_pos) <= d + 2:
        new_points.append((x - 1, y))
    p3 = (x, y + 1)
    if manheten_length(*p3, *target_pos) <= d + 2:
        new_points.append((x, y + 1))
    p4 = (x, y - 1)
    if manheten_length(*p4, *target_pos) <= d + 2:
        new_points.append((x, y - 1))
    mapp += new_points
    for point in new_points:
        s += list(set(mapp + generate_path(*point, t - 1, mapp, target_pos)))
    return list(set(mapp + s))


def generate_path_2(x, y, t, mapp):
    s = []
    new_points = []
    if t == 0:
        return list(set(mapp + [(0, 0)]))
    new_points.append((x + 1, y))
    new_points.append((x - 1, y))
    new_points.append((x, y + 1))
    new_points.append((x, y - 1))
    mapp += new_points
    for point in new_points:
        s += list(set(mapp + generate_path_2(*point, t - 1, mapp)))
    return list(set(mapp + s))


def generate_pos(x, y):
    new_points = []
    new_points.append((x + 1, y))
    new_points.append((x - 1, y))
    new_points.append((x, y + 1))
    new_points.append((x, y - 1))
    new_points.append((x, y))
    return new_points


t, d, n = map(int, input().split())
ans = []
sp = []
for i in range(n):
    x, y = map(int, input().split())
    sp.append((x, y))

if len(sp) >= 2:
    prev_pos = sp[-2]
    curr_pos = sp[-1]
    n_pos = generate_pos(*prev_pos)
    ans = []
    for pos in n_pos:
        if manheten_length(*pos, *curr_pos) <= d + 2 and pos not in ans:
            ans += generate_path(*pos, 2, [], curr_pos)
    res = set(cut_points(*curr_pos, d, ans))
else:
    res = generate_path_2(*sp[0], t, [])
print(len(res))
for elem in res:
    print(*elem)
