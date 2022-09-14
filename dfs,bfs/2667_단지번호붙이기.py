import sys
from collections import deque

V = int(sys.stdin.readline())
lst_N = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(V)]

dr = [0, 0, 1, -1]
dc = [-1, 1, 0, 0]
visited = [[0]*(V) for _ in range(V)]

def bfs(r, c):
    global V
    Q = deque()
    Q.append((r,c))
    visited[r][c] = 1
    cnt = 1

    while Q:
        r2, c2 = Q.popleft()
        for i in range(4):
            r3 = r2 + dr[i]
            c3 = c2 + dc[i]
            if 0 <= r3 < V and 0 <= c3 < V and lst_N[r3][c3] == 1 and visited[r3][c3] == 0:
                visited[r3][c3] = 1
                Q.append((r3, c3))
                cnt += 1

    return cnt


ans = []
for r in range(V):
    for c in range(V):
        if lst_N[r][c] == 1 and visited[r][c] == 0:
            ans += [bfs(r, c)]

ans.sort()
print(len(ans))
for i in ans:
    print(i)