import sys

def lotto(level):
    global cnt, result
    if level == 6:
        cnt += 1
        print(*path)
        return
    for i in range(1, k+1):
        if level > 0 and path[level - 1] >= arr_k[i]:
            continue
        path[level] = arr_k[i]
        lotto(level+1)
        path[level] = ''

while True:
    arr_k = list(map(int, sys.stdin.readline().split()))
    if 0 in arr_k:
        break
    k = arr_k[0]
    cnt = 0
    path = [''] * 6
    result = []
    lotto(0)
    print()