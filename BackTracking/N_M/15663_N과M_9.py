import sys

N, M = map(int, sys.stdin.readline().split())

lst_N = sorted(list(map(int, sys.stdin.readline().split())))
path = [''] * M
comp_lst = []
used = [0] * N

def nm(level):
    global comp_lst
    if level == M:
        tmp_lst = []
        for j in range(M):
            tmp_lst.append(path[j])
            comp_lst.append(tmp_lst)
        return
    for i in range(N):
        if used[i] == 1:
            continue
        used[i] = 1
        path[level] = lst_N[i]
        nm(level+1)
        used[i] = 0

nm(0)
tmp_lst2 = list(set([tuple(i) for i in comp_lst]))

for i in range(len(tmp_lst2)):
    tmp_lst2[i] = list(tmp_lst2[i])
if M == 1:
    tmp_lst2.sort(key = lambda x:x[0])
elif M == 2:
    tmp_lst2.sort(key = lambda x:(x[0], x[1]))
elif M == 3:
    tmp_lst2.sort(key = lambda x:(x[0], x[1], x[2]))
elif M == 4:
    tmp_lst2.sort(key = lambda x:(x[0], x[1], x[2], x[3]))
elif M == 5:
    tmp_lst2.sort(key = lambda x:(x[0], x[1], x[2], x[3], x[4]))
elif M == 6:
    tmp_lst2.sort(key = lambda x:(x[0], x[1], x[2], x[3], x[4], x[5]))
elif M == 7:
    tmp_lst2.sort(key = lambda x:(x[0], x[1], x[2], x[3], x[4], x[5], x[6]))
elif M == 8:
    tmp_lst2.sort(key = lambda x:(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7]))

for j in tmp_lst2:
    print(*j)

