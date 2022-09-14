import sys
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
dd = [1, -1]

M, N, H = map(int, sys.stdin.readline().split())
box = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]

tomato_lst = []
for d in range(H):
    for r in range(N):
        for c in range(M):
            if box[d][r][c] == 1:
                tomato_lst.append([d, r, c])

def bfs(lst):
    Q = deque()

    for i in tomato_lst:
        Q.append(i)

    while Q:
        d, r, c = Q.popleft()
        for i in range(4):
            r2 = r + dr[i]
            c2 = c + dc[i]
            if 0 <= r2 < N and 0 <= c2 < M and box[d][r2][c2] == 0:
                box[d][r2][c2] = box[d][r][c] + 1
                Q.append([d, r2, c2])
        for j in range(2):
            d2 = d + dd[j]
            if 0 <= d2 < H and box[d2][r][c] == 0:
                box[d2][r][c] = box[d][r][c] + 1
                Q.append([d2, r, c])

bfs(tomato_lst)
ans = 0

for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 0:
                ans = -1
                break
        if ans == -1:
            break
        elif ans < max(box[i][j]):
            ans = max(box[i][j])

if ans == -1:
    print(ans)
else:
    print(ans-1)