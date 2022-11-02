import sys

N, M = map(int, sys.stdin.readline().split())

lst_N = [i for i in range(1, N+1)]
path = [''] * M
used = [0] * N

def nm(level, start):
    if level == M:
        for j in range(M):
            print(path[j], end = ' ')
        print()
        return
    for i in range(start, N):
        path[level] = lst_N[i]
        nm(level+1, i+1)

nm(0, 0)