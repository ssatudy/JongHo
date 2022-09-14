import sys
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

y, x = map(int, sys.stdin.readline().split())
map = [list(map(int, sys.stdin.readline().split())) for _ in range(y)]

def bfs(r, c):
    global visited, amount
    Q = deque()
    Q.append([r,c])

    while Q:
        r1, c1 = Q.popleft()
        for i in range(4):
            r2 = r1 + dr[i]
            c2 = c1 + dc[i]
            if 0 <= r2 < y and 0 <= c2 < x and not visited[r2][c2]:
                if map[r2][c2] == 1:
                    melt_xy.append([r2, c2])
                    amount += 1
                    visited[r2][c2] = True
                elif map[r2][c2] == 0:
                    Q.append([r2,c2])
                    visited[r2][c2] = True


for r in range(y):
    for c in range(x):
        if map[r][c] == 0:
            a, b = r, c
            break
        break

cnt = 0
melt_amount = []
while True:
    cnt += 1
    visited = [[False] * x for _ in range(y)]
    melt_xy = []
    amount = 0
    bfs(a, b)
    if len(melt_xy) == 0:
        break
    else:
        for i in melt_xy:
            map[i[0]][i[1]] = 0
    melt_amount.append(amount)


print(cnt -1)
print(melt_amount[-1])