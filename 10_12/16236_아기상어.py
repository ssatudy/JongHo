import sys
from collections import deque

d = [(-1, 0), (0, -1), (0, 1), (1, 0)]


def bfs(r, c, cnt):
    global ans, comp_catch, size
    Q = deque()
    Q.append((r, c, cnt))
    visited = [[False] * N for _ in range(N)]
    visited[r][c] = True
    catch_lst = []
    load_lst = []
    catch_v = 0
    comp_lst = [[True] * N for _ in range(N)]

    while Q:
        r, c, cnt = Q.popleft()
        if cnt > (N ** 2) or visited == comp_lst:
            break
        if len(Q) == 0:
            for i in d:
                r2 = r + i[0]
                c2 = c + i[1]
                if 0 <= r2 < N and 0 <= c2 < N and 1 <= lst_N[r2][c2] < size and not visited[r2][c2]:
                    visited[r2][c2] = True
                    catch_lst.append([r2, c2, cnt + 1])
                elif 0 <= r2 < N and 0 <= c2 < N and not visited[r2][c2] and (lst_N[r2][c2] == 0 or lst_N[r2][c2] == size) and len(catch_lst) == 0:
                    visited[r2][c2] = True
                    load_lst.append([r2, c2, cnt + 1])
            if len(catch_lst) != 0:
                catch_lst.sort()
                lst_N[catch_lst[0][0]][catch_lst[0][1]] = 0
                ans += catch_lst[0][2]
                catch_v += 1
                if catch_v == size:
                    catch_v = 0
                    size += 1
                visited = [[False] * N for _ in range(N)]
                visited[catch_lst[0][0]][catch_lst[0][1]] = True
                Q = deque()
                Q.append([catch_lst[0][0], catch_lst[0][1], 0])
                catch_lst = []
                load_lst = []
            else:
                visited = [[False] * N for _ in range(N)]
                for i in load_lst:
                    Q.append([i[0], i[1], i[2]])
                catch_lst = []
                load_lst = []
        else:
            for i in d:
                r2 = r + i[0]
                c2 = c + i[1]
                if 0 <= r2 < N and 0 <= c2 < N and 1 <= lst_N[r2][c2] < size and not visited[r2][c2]:
                    visited[r2][c2] = True
                    catch_lst.append([r2, c2, cnt + 1])
                elif 0 <= r2 < N and 0 <= c2 < N and not visited[r2][c2] and (lst_N[r2][c2] == 0 or lst_N[r2][c2] == size) and len(catch_lst) == 0:
                    visited[r2][c2] = True
                    load_lst.append([r2, c2, cnt + 1])


N = int(sys.stdin.readline())

lst_N = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
comp_catch = 0
ans = 0
size = 2

for r in range(N):
    for c in range(N):
        if lst_N[r][c] == 9:
            lst_N[r][c] = 0
            bfs(r, c, 0)

print(ans)
