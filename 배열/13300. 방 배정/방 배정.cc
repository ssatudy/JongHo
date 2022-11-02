#include<iostream>
#include<bits/stdc++.h>

using namespace std;
int arr[2][6];

int main() {
    ios_base :: sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int N, k, ans = 0;
    cin >> N;
    cin >> k;
    int sex, grade;
    for (int i = 0; i < N; i ++) {
        cin >> sex;
        cin >> grade;
        arr[sex][grade - 1] += 1;
    }
    for (int r = 0; r < 2; r++) {
        for (int c = 0; c < 6; c++) {
            if (0 < arr[r][c] && arr[r][c] <= k) {
                ans += 1;
            }
            else if (arr[r][c] > k) {
                int tmp, tmp2;
                tmp = arr[r][c] / k;
                tmp2 = arr[r][c] % k;
                if (tmp2 > 0) {
                    ans += tmp + 1;
                }
                else {
                    ans += tmp;
                }
            }
        }
    }

    cout << ans;
    return 0;
}
