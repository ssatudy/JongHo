import sys

N, K = map(int, sys.stdin.readline().split())
lst_N = [[0, 0] for _ in range(7)]
for i in range(N):
    sex, cls = map(int, sys.stdin.readline().split())
    lst_N[cls][sex] += 1

ans = 0
for i in range(1, len(lst_N)):
    for j in range(2):
        if lst_N[i][j] == 0:
            continue
        elif lst_N[i][j] % K:
           ans += lst_N[i][j] // K + 1
        else:
           ans += lst_N[i][j] // K

print(ans)