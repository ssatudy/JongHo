import sys
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

T = int(sys.stdin.readline())

def bfs(y, x):
    global M, N
    visited[y][x] = True
    Q = deque()
    Q.append((y, x))

    while Q:
        a, b = Q.popleft()
        for i in range(4):
            a2 = a + dr[i]
            b2 = b + dc[i]
            if 0 <= a2 < N and 0 <= b2 < M and not visited[a2][b2] and lst_a[a2][b2] == 1:
                visited[a2][b2] = True
                Q.append((a2, b2))

    return 1


for tc in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    lst_a = [[0] * M for _ in range(N)]
    for _ in range(K):
        u, v = map(int, sys.stdin.readline().split())
        lst_a[v][u] = 1
    visited = [[False] * M for _ in range(N)]
    ans = 0
    for r in range(N):
        for c in range(M):
            if lst_a[r][c] == 1 and not visited[r][c]:
                ans += bfs(r, c)
    print(ans)