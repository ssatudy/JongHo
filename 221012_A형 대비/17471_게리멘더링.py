import sys
from itertools import combinations
from collections import deque

def bfs(lst, devi):
    global sum_a, sum_b
    Q = deque()
    value = lst[0]
    visited = set()
    visited.add(value)
    if not devi:
        sum_a += lst_value[value]
    else:
        sum_b += lst_value[value]
    Q.append(value)

    while Q:
        value = Q.popleft()
        for i in G[value]:
            if i not in visited and i in lst:
                if not devi:
                    sum_a += lst_value[i]
                else:
                    sum_b += lst_value[i]
                Q.append(i)
                visited.add(i)

    return len(visited)


N = int(sys.stdin.readline())
lst_value = [0] + list(map(int, sys.stdin.readline().split()))
al_sum = sum(lst_value)

G = [[] for _ in range(N + 1)]
cnt = []
ans = al_sum + 1
for i in range(1, N + 1):
    tmp_lst = list(map(int, sys.stdin.readline().split()))
    if len(tmp_lst) == 1:
        cnt.append(i)
    if len(cnt) > 0:
        break
    for j in range(1, tmp_lst[0] + 1):
        G[i].append(tmp_lst[j])

if len(cnt) > 1:
    print(-1)
else:
    num_lst = [i for i in range(1, N + 1)]
    for i in range(1, N):
        check_lst1 = list(combinations(num_lst, i))
        for j in check_lst1:
            sum_a, sum_b = 0, 0
            len_a = bfs(j, 0)
            check_lst2 = tuple(i for i in range(1, N + 1) if i not in j)
            len_b = bfs(check_lst2, 1)
            if len_a + len_b == N:
                ans = min(ans, abs(sum_a - sum_b))
    if ans == al_sum + 1:
        ans = -1
print(ans)

