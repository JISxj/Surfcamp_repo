def watch(board, x, y):
    if board[x][y] == "*":
        return 1
    return 0


def count_mines(_board, _i, _j):
    ans = 0
    if _i > 0:
        ans += watch(board, _i - 1, _j)
    if _i < len(_board) - 1:
        ans += watch(board, _i + 1, _j)
    if _j < len(board[0]) - 1:
        ans += watch(board, _i, _j + 1)
    if _j > 0:
        ans += watch(board, _i, _j - 1)
    if _i > 0 and _j > 0:
        ans += watch(board, _i - 1, _j - 1)
    if _i < len(_board) - 1 and _j > 0:
        ans += watch(board, _i + 1, _j - 1)
    if _i > 0 and _j < len(board[0]) - 1:
        ans += watch(board, _i - 1, _j + 1)
    if _i < len(board) - 1 and _j < len(board[0]) - 1:
        ans += watch(board, _i + 1, _j + 1)
    return ans


st = list(map(int, input().split()))
n, m, k = st[0], st[1], st[2]

mine_coords = []
for i in range(k):
    mine_coords.append(list(map(int, input().split())))

board = []
for i in range(n):
    board.append([])
    for j in range(m):
        board[i].append(0)


for i in range(k):
    board[mine_coords[i][0] - 1][mine_coords[i][1] - 1] = "*"

for i in range(n):
    for j in range(m):
        if board[i][j] != "*":
            board[i][j] = count_mines(board, i, j)
        print(board[i][j], end=" ")
    print()

