import sys
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

M, N, K = map(int, sys.stdin.readline().split())

paper = [[0] * N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for r in range(y1, y2):
        for c in range(x1, x2):
            paper[r][c] = 1

def bfs(r, c):
    global size
    Q = deque()
    Q.append([r,c])
    paper[r][c] = 1

    while Q:
        size += 1
        r, c = Q.popleft()
        for i in range(4):
            c2 = c + dc[i]
            r2 = r + dr[i]
            if 0 <= c2 < N and 0 <= r2 < M and paper[r2][c2] == 0:
                Q.append([r2, c2])
                paper[r2][c2] = 1

    return 1

ans = 0
size = 0
size_lst = []
for r in range(M):
    for c in range(N):
        if paper[r][c] == 0:
            ans += bfs(r, c)
            if size != 0:
                size_lst.append(size)
            size = 0
size_lst.sort()
print(ans)
print(*size_lst)
