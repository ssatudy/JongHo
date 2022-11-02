def searchMax(i, cnt, value):
    global max_tmp, C
    if cnt <= C:
        max_tmp = max(value, max_tmp)
    if cnt > C:
        return
    for j in range(i+1, M):
        if not visited_tmp[j]:
            visited_tmp[j] = True
            searchMax(j, cnt + a_lst[j], value + a_lst[j] ** 2)
            visited_tmp[j] = False


for tc in range(1, int(input()) + 1):
    N, M, C = map(int, input().split())
    lst_N = [list(map(int, input().split())) for _ in range(N)]
    tmp_lst = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            tmp_lst[r][c] = lst_N[r][c] ** 2
    for r in range(N):
        for c in range(N - M + 1):
            tmp_M = M
            if sum(lst_N[r][c:c+tmp_M]) > C:
                a_lst = sorted(lst_N[r][c:c+tmp_M])
                max_tmp = 0
                for i in range(M):
                    visited_tmp = [False] * M
                    visited_tmp[i] = True
                    searchMax(i, a_lst[i], a_lst[i] ** 2)
                tmp_lst[r][c] = max_tmp
            elif sum(lst_N[r][c:c+tmp_M]) <= C:
                tmp_lst[r][c] = sum(tmp_lst[r][c:c+tmp_M])

    max_v1 = 0
    v1_rc = 0
    max_v2 = 0
    visited = [[False] * N for _ in range(N)]
    for i in range(len(tmp_lst)):
        if max(tmp_lst[i]) > max_v1:
            max_v1 = max(tmp_lst[i])
            v1_rc = [i, tmp_lst[i].index(max(tmp_lst[i]))]

    for i in range(v1_rc[1], v1_rc[1] + M):
        if 0 <= i < N:
            visited[v1_rc[0]][i] = True

    for i in range(len(tmp_lst)):
        if max(tmp_lst[i]) > max_v2 and not visited[i][tmp_lst[i].index(max(tmp_lst[i]))]:
            max_v2 = max(tmp_lst[i])
    ans = max_v2 + max_v1

    print(f'#{tc}', ans)