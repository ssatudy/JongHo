#include <iostream>
#include <bits/stdc++.h>

using namespace std;


int main() {
    ios_base :: sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int N;
    cin >> N;
    string alphabet;
    alphabet = "abcdefghijklmnopqrstuvwxyz";
    for (int i = 0; i < N; i++) {
        int alphaA[26] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
        int alphaB[26] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
        string A, B;
        cin >> A;
        cin >> B;
        for (int k = 0; k < A.length(); k++) {
            for (int j = 0; j < 26; j++) {
                if (alphabet[j] == A[k]) {
                    alphaA[j] += 1;
                }
            }
        }
        for (int l = 0; l < B.length(); l++) {
            for (int j = 0; j < 26; j++) {
                if (alphabet[j] == B[l]) {
                    alphaB[j] += 1;
                }
            }
        }
        bool ans;
        ans = true;
        for (int m = 0; m < 26; m++) {
            if (alphaA[m] != alphaB[m]) {
                ans = false;
                break;
            }
        }
        if (ans) {
            cout << "Possible" << endl;
        }
        else {
            cout << "Impossible" << endl;
        }
    }

    return 0;
}
