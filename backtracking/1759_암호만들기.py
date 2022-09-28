import sys

dic_abc = {'a':0, 'b':1, 'c':1, 'd':1, 'e':0, 'f':1,
           'g':1, 'h':1, 'i':0, 'j':1, 'k':1, 'l':1,
           'm':1, 'n':1, 'o':0, 'p':1, 'q':1, 'r':1,
           's':1, 't':1, 'u':0, 'v':1, 'w':1, 'x':1,
           'y':1, 'z':1
           }

def dfs(value, cnt_a, cnt_b, idx):
    if len(value) == L:
        if cnt_a < 1 or cnt_b < 2:  return
        else:
            print(value)
        return
    for i in range(idx, C):
        if not used[i]:
            used[i] = 1
            if dic_abc[lst_C[i]] == 1:
                dfs(value + lst_C[i], cnt_a, cnt_b + 1, i)
                used[i] = 0
            else:
                dfs(value + lst_C[i], cnt_a + 1, cnt_b, i)
                used[i] = 0

L, C = map(int, sys.stdin.readline().split())
lst_C = sorted(list(map(str, sys.stdin.readline().split())))
used = [0] * C
dfs('', 0, 0, 0)