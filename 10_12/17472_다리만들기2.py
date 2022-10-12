import sys
from collections import deque

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

def bfs(r, c):
    global clr_num
    Q = deque()
    Q.append([r, c])
    color[r][c] = True
    map_lst[r][c] = clr_num

    while Q:
        r, c = Q.popleft()
        for i in range(4):
            r2 = r + dr[i]
            c2 = c + dc[i]
            if 0 <= r2 < N and 0 <= c2 < M and not color[r2][c2] and map_lst[r2][c2] == 1:
                color[r2][c2] = True
                map_lst[r2][c2] = clr_num
                Q.append([r2, c2])

def searchWeight(r, c, dir, cnt, pre_v):
    while True:
        r += dr[dir]
        c += dc[dir]
        if 0 <= r < N and 0 <= c < M and map_lst[r][c] == 0:
            cnt += 1
        elif 0 <= r < N and 0 <= c < M and map_lst[r][c] != pre_v and cnt > 1:
            weight_lst.append([pre_v, map_lst[r][c], cnt])
            break
        else:
            break



N, M = map(int, sys.stdin.readline().split())

map_lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

color = [[False] * M for _ in range(N)]
clr_num = 1
for r in range(N):
    for c in range(M):
        if map_lst[r][c] == 1:
            clr_num += 1
            bfs(r, c)

weight_lst = []
check_num = [0, 0] + [i for i in range(2, clr_num + 1)]


for r in range(N):
    for c in range(M):
        if r - 1 >= 0 and map_lst[r - 1][c] == 0 and map_lst[r][c] != 0:
            searchWeight(r - 1, c, 2, 1, map_lst[r][c])
        if r + 1 < N and map_lst[r + 1][c] == 0 and map_lst[r][c] != 0:
            searchWeight(r + 1, c, 3, 1, map_lst[r][c])
        if c + 1 < M and map_lst[r][c + 1] == 0 and map_lst[r][c] != 0:
            searchWeight(r, c + 1, 0, 1, map_lst[r][c])
        if c - 1 >= 0 and map_lst[r][c - 1] == 0 and map_lst[r][c] != 0:
            searchWeight(r, c - 1, 1, 1, map_lst[r][c])

weight_lst.sort(key= lambda x: x[2])

checking = [0, 0] + [2] * (clr_num + 1 - 2)
ans = 0

for i in weight_lst:
    a, b, weight = i[0], i[1], i[2]
    if check_num[a] != check_num[b]:
        ans += weight
        if check_num[a] < check_num[b]:
            target = check_num[b]
            for i in range(2, len(check_num)):
                if check_num[i] == target:
                    check_num[i] = check_num[a]
        elif check_num[a] > check_num[b]:
            target = check_num[a]
            for i in range(2, len(check_num)):
                if check_num[i] == target:
                    check_num[i] = check_num[b]

if check_num != checking:
    ans = -1

print(ans)