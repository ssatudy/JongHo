#include<iostream>
#include<bits/stdc++.h>

using namespace std;

int main() {
    ios_base :: sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int n, ans = 0;
    int arr[n];
    cin >> n;
    for (int i = 0; i < n; i++) {
        int num;
        cin >> num;
        arr[i] = num;
    }
    int target = 0;
    cin >> target;
    for (int j = 0; j < n; j++) {
        if (arr[j] == target) {
            ans += 1;
        }
    }

    cout << ans;
    return 0;
}
