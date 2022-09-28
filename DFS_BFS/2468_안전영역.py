import sys
from collections import deque


def bfs(r, c):
    global N, visited
    Q = deque()
    Q.append([r, c])
    visited[r][c] = True

    while Q:
        r1, c1 = Q.popleft()
        for i in range(4):
            r2 = r1 + dr[i]
            c2 = c1 + dc[i]
            if 0 <= r2 < N and 0 <= c2 < N and not visited[r2][c2]:
                Q.append([r2, c2])
                visited[r2][c2] = True

    return 1

ans_lst = []

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N = int(sys.stdin.readline())

area = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
for value in range(101):
    visited = [[False] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if area[r][c] <= value:
                visited[r][c] = True

    ans = 0
    for r in range(N):
        for c in range(N):
            if area[r][c] > value and not visited[r][c]:
                ans += bfs(r, c)
    ans_lst.append(ans)

print(max(ans_lst))