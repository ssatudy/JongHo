import sys

def dfs(level, value):
    global ans
    if level == 10:
        if value > ans:
            ans = value
        return
    for i in range(11):
        if not visited[i] and lst_N[level + 1][i] != 0:
            visited[i] = True
            dfs(level + 1, value + lst_N[level + 1][i])
            visited[i] = False

ans_lst = []

for tc in range(int(sys.stdin.readline())):
    lst_N = [list(map(int, sys.stdin.readline().split())) for _ in range(11)]
    ans = 0
    for i in range(11):
        if lst_N[0][i] != 0:
            visited = [False] * 11
            visited[i] = True
            dfs(0, lst_N[0][i])
    ans_lst.append(f'{ans}')

print('\n'.join(ans_lst))