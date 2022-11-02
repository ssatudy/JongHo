import sys

N, M = map(int, sys.stdin.readline().split())

lst_N = sorted(list(map(int, sys.stdin.readline().split())))
path = [''] * M
comp_lst = []

def nm(level):
    global comp_lst
    if level == M:
        tmp_lst = []
        for j in range(M):
            tmp_lst.append(path[j])
        if tmp_lst not in comp_lst:
            print(*tmp_lst)
            comp_lst.append(tmp_lst)
        return
    for i in range(N):
        if level > 0 and path[level -1] > lst_N[i]:
            continue
        path[level] = lst_N[i]
        nm(level+1)

nm(0)