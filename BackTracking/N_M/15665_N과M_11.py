import sys

N, M = map(int, sys.stdin.readline().split())

lst_N = sorted(list(map(int, sys.stdin.readline().split())))
path = [''] * M
tmp_lst2 = []

def nm(level):
    global comp_lst
    if level == M:
        tmp_lst = []
        for j in range(M):
            tmp_lst.append(path[j])
        tmp_lst2.append(tmp_lst)
        return
    for i in range(N):
        path[level] = lst_N[i]
        nm(level+1)

nm(0)

tmp_lst2 = list(set([tuple(i) for i in tmp_lst2]))

for i in range(len(tmp_lst2)):
    tmp_lst2[i] = list(tmp_lst2[i])

for k in range(M-1, -1, -1):
    tmp_lst2.sort(key=lambda x:x[k])

for j in tmp_lst2:
    print(*j)