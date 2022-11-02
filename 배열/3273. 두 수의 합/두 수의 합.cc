#include<iostream>
#include<bits/stdc++.h>

using namespace std;

int main() {
    ios_base :: sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    long n;
    cin >> n;
    int arr[n];
    for (int i=0; i < n; i++) {
        long Num;
        cin >> Num;
        arr[i] = Num;
    }
    sort(arr, arr + n);
    long target;
    long ans = 0;
    cin >> target;
    long first = 0;
    long last = n - 1;
    while (true) {
        if (first >= last) {
            break;
        }
        else {
            if (arr[first] + arr[last] == target) {
                ans += 1;
                first += 1;
            }
            else if (arr[first] + arr[last] > target) {
                last -= 1;
            }
            else {
                first += 1;
            }
        }
    }
    cout << ans;
    return 0;
}
