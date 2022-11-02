import sys
from collections import deque

def bfs(N, level):
    global ans, check_lst, check_len
    Q = deque()
    Q.append([N, level])

    while Q:
        n, level = Q.popleft()
        check_lst.add(n)
        check_len += 1
        if check_len == len(check_lst):
            if n == K:
               if ans > level:
                   ans = level
            if n * 2 < K * 2 and level < ans:
                Q.append([n * 2, level + 1])
            if n < K and level < ans:
                Q.append([n + 1, level + 1])
            if n > 0 and level < ans:
                Q.append([n - 1, level + 1])
        else:
            check_len -= 1

N, K = map(int, sys.stdin.readline().split())
ans = 99999999
check_lst = set()
check_len = len(check_lst)
bfs(N, 0)
print(ans)