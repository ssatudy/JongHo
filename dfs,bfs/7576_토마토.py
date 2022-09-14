import sys
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

def bfs(lst):
    Q = deque()
    for i in lst:
        Q.append(i)

    while Q:
        r, c = Q.popleft()
        for j in range(4):
            r2 = r + dr[j]
            c2 = c + dc[j]
            if 0 <= r2 < N and 0 <= c2 < M and lst_N[r2][c2] == 0:
                lst_N[r2][c2] = lst_N[r][c] +1
                Q.append([r2, c2])

M, N = map(int, sys.stdin.readline().split())
lst_N = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

tmp_lst = []
for r in range(N):
    for c in range(M):
        if lst_N[r][c] == 1:
            tmp_lst.append([r, c])

bfs(tmp_lst)

ans = 0
for i in range(N):
    for j in range(M):
        if lst_N[i][j] == 0:
            ans = -1
            break
    if ans == -1:
        break
    ans = max(ans, max(lst_N[i]))

if ans == -1:
    print(ans)
else:
    print(ans-1)