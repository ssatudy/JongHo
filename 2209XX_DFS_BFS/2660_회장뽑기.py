import sys
from collections import deque

V = int(sys.stdin.readline())

N = V + 1
G = [[] for _ in range(N)]

while True:
    u, v = map(int, sys.stdin.readline().split())
    if u == -1 and v == -1:
        break
    G[u].append(v)
    G[v].append(u)

def bfs(v):
    global N, point
    Q = deque()
    visited[v] = 1
    Q.append(v)
    while Q:
        v = Q.popleft()
        for w in G[v]:
            if not visited[w]:
                Q.append(w)
                visited[w] = visited[v] + 1
                point = visited[v] + 1
    return point

point_lst=[]
for i in range(1, N):
    point = 0
    visited = [0] * N
    point_lst.append(bfs(i))

min_point = min(point_lst)

ans_lst = []
for idx, value in enumerate(point_lst):
    if value == min_point:
        ans_lst.append(idx+1)

print(min_point-1, len(ans_lst))
print(*ans_lst)