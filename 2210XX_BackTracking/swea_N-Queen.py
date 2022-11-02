def Queen(r):
    global ans
    if r == N:
        ans += 1

    for c in range(N):
        if cols[c]:
            continue
        line1_check = r + c
        line2_check = r - c + (N-1)
        if line1[line1_check] or line2[line2_check]:
            continue
        cols[c] = line1[line1_check] = line2[line2_check] = 1
        Queen(r+ 1)
        cols[c] = line1[line1_check] = line2[line2_check] = 0

ans_lst = []
for tc in range(1, int(input())+1):
    N = int(input())
    cols = [0] * N
    line1 = [0] * (N+N)
    line2 = [0] * (N+N)
    ans = 0
    Queen(0)
    ans_lst.append(f'#{tc} {ans}')

print('\n'.join(ans_lst))