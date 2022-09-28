import sys

N, M = map(int, sys.stdin.readline().split())

lst_N = sorted(list(map(int, sys.stdin.readline().split())))
path = [''] * M

def nm(level):
    if level == M:
        for j in range(M):
            print(path[j], end = ' ')
        print()
        return
    for i in range(N):
        if level > 0 and path[level-1] >= lst_N[i]:
            continue
        path[level] = lst_N[i]
        nm(level+1)

nm(0)