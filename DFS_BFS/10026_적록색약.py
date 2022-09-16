import sys
from collections import deque

dr = [0, 0, 1, -1]
dc = [-1, 1, 0, 0]

N = int(sys.stdin.readline())
lst_N = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
visited2 = [[False] * N for _ in range(N)]
normal_ans = 0
abnormal_ans = 0

def normal(a, b, value):
    global normal_ans
    Q = deque()
    Q.append((a, b))
    visited[a][b] = True

    while Q:
        r, c = Q.popleft()
        for i in range(4):
            r2 = r + dr[i]
            c2 = c + dc[i]
            if 0 <= r2 < N and 0 <= c2 < N and not visited[r2][c2] and lst_N[r2][c2] == value:
                Q.append((r2, c2))
                visited[r2][c2] = True

    normal_ans += 1

def abnormal(a, b, value):
    global abnormal_ans
    if value == 'G' or value == 'R':
        Q = deque()
        Q.append((a, b))
        visited2[a][b] = True

        while Q:
            r, c = Q.popleft()
            for i in range(4):
                r2 = r + dr[i]
                c2 = c + dc[i]
                if 0 <= r2 < N and 0 <= c2 < N and not visited2[r2][c2] and (lst_N[r2][c2] == 'G' or lst_N[r2][c2] == 'R'):
                    Q.append((r2, c2))
                    visited2[r2][c2] = True

        abnormal_ans += 1
    else:
        Q = deque()
        Q.append((a, b))
        visited2[a][b] = True

        while Q:
            r, c = Q.popleft()
            for i in range(4):
                r2 = r + dr[i]
                c2 = c + dc[i]
                if 0 <= r2 < N and 0 <= c2 < N and not visited2[r2][c2] and lst_N[r2][c2] == value:
                    Q.append((r2, c2))
                    visited2[r2][c2] = True

        abnormal_ans += 1


for r in range(N):
    for c in range(N):
        if visited[r][c] == False:
            normal(r, c, lst_N[r][c])
        if visited2[r][c] == False:
            abnormal(r, c, lst_N[r][c])



print(normal_ans, abnormal_ans)