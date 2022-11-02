dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def searchProc(proc_num, core, length, cnt):
    global ans_core, ans_length
    if proc_num == len(proc_lst):
        if core > 0:
            if ans_core < core:
                ans_core = core
                ans_length = length
            elif ans_core == core:
                ans_length = min(ans_length, length)
        return
    elif ans_core > core + (len(proc_lst) - proc_num):
        return
    r, c = proc_lst[proc_num]
    for i in range(4):
        direct = i
        core, length = Install(r, c, direct, core, length, cnt)
        searchProc((proc_num + 1), core, length, cnt + 1)
        core, length = Undo(r, c, direct, core, length, cnt)


def Install(r, c, direct, core, length, cnt):
    r2 = r + dr[direct]
    c2 = c + dc[direct]
    TF = True
    if 0 <= r2 < N and 0 <= c2 < N and lst_N[r2][c2] == 0:
        lst_N[r2][c2] = cnt
        length += 1
        if r2 == 0 or c2 == 0 or r2 == N - 1 or c2 == N - 1:
            core += 1
            return core, length
        while True:
            r2 += dr[direct]
            c2 += dc[direct]
            if 0 <= r2 < N and 0 <= c2 < N and lst_N[r2][c2] == 0:
                length += 1
                lst_N[r2][c2] = cnt
                if r2 == 0 or c2 == 0 or r2 == N - 1 or c2 == N - 1:
                    core += 1
                    break
            else:
                TF = False
                break
        if not TF:
            core, length = Undo(r, c, direct, core, length, cnt)
    return core, length


def Undo(r, c, direct, core, length, cnt):
    r2 = r + dr[direct]
    c2 = c + dc[direct]
    if 0 <= r2 < N and 0 <= c2 < N and lst_N[r2][c2] == cnt:
        lst_N[r2][c2] = 0
        length -= 1
        if r2 == 0 or c2 == 0 or r2 == N - 1 or c2 == N - 1:
            core -= 1
            return core, length
        while True:
            r2 += dr[direct]
            c2 += dc[direct]
            if 0 <= r2 < N and 0 <= c2 < N and lst_N[r2][c2] == cnt:
                lst_N[r2][c2] = 0
                length -= 1
                if r2 == 0 or c2 == 0 or r2 == N - 1 or c2 == N - 1:
                    core -= 1
                    break
            else:
                break
    return core, length

for tc in range(1, int(input()) + 1):
    N = int(input())
    lst_N = [list(map(int, input().split())) for _ in range(N)]
    proc_lst = []
    for r in range(1, N - 1):
        for c in range(1, N - 1):
            if lst_N[r][c]:
                proc_lst.append([r, c])
    ans_core = 0
    ans_length = 99999
    searchProc(0, 0, 0, 2)
    print(f'#{tc}', ans_length)