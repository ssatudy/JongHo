import sys

N, M = map(int, sys.stdin.readline().split())

lst_N = sorted(list(map(int, sys.stdin.readline().split())))
path = [''] * M
used = [0] * N

def nm(level):
    if level == M:
        for j in range(M):
            print(path[j], end = ' ')
        print()
        return
    for i in range(N):
        if used[i] == 1:
            continue
        used[i] = 1
        path[level] = lst_N[i]
        nm(level+1)
        used[i] = 0

nm(0)