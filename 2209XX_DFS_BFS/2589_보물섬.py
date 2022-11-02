import sys
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

y, x = map(int, sys.stdin.readline().split())
map = [list(sys.stdin.readline().rstrip()) for _ in range(y)]
for r in range(y):
    for c in range(x):
        if map[r][c] == 'W':
            map[r][c] = -1
        else:
            map[r][c] = 0

def bfs(r, c):
    global visited
    Q = deque()
    Q.append([r, c])
    visited[r][c] = 1

    while Q:
        r1, c1 = Q.popleft()
        for i in range(4):
            r2 = r1 + dr[i]
            c2 = c1 + dc[i]
            if 0 <= r2 < y and 0 <= c2 < x and visited[r2][c2] == 0:
                Q.append([r2, c2])
                visited[r2][c2] = visited[r1][c1] + 1


ans = 0

for r in range(y):
    for c in range(x):
        if map[r][c] == 0:
            visited = [[0] * x for _ in range(y)]
            for a in range(y):
                for b in range(x):
                    if map[a][b] == -1:
                        visited[a][b] = -1
            bfs(r, c)
            for r2 in range(y):
                if ans < max(visited[r2]):
                    ans = max(visited[r2])

print(ans-1)