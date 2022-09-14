import sys

V = int(sys.stdin.readline())
E = int(sys.stdin.readline())

G = [[] for _ in range(V+1)]
visited = [0] * (V+1)

for _ in range(E):
    u, v = map(int, sys.stdin.readline().split())
    G[u].append(v)
    G[v].append(u)

ans = -1
def dfs(v):
    global ans
    visited[v] = 1
    ans += 1
    for w in G[v]:
        if not visited[w]:
            dfs(w)

dfs(1)

print(ans)