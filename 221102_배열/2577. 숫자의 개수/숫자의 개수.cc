#include<iostream>
#include<bits/stdc++.h>

using namespace std;
int Num[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};


int main() {
    int A, B, C, multi;
    cin >> A;
    cin >> B;
    cin >> C;
    multi = A * B * C;
    string stM;
    stM = to_string(multi);
    for (int i = 0; i < stM.length(); i++) {
        if (stM[i] == '0') {
            Num[0] += 1;
        }
        else if (stM[i] == '1') {
            Num[1] += 1;
        }
        else if (stM[i] == '2') {
            Num[2] += 1;
        }
        else if (stM[i] == '3') {
            Num[3] += 1;
        }
        else if (stM[i] == '4') {
            Num[4] += 1;
        }
        else if (stM[i] == '5') {
            Num[5] += 1;
        }
        else if (stM[i] == '6') {
            Num[6] += 1;
        }
        else if (stM[i] == '7') {
            Num[7] += 1;
        }
        else if (stM[i] == '8') {
            Num[8] += 1;
        }
        else if (stM[i] == '9') {
            Num[9] += 1;
        }
    }
    for (int j = 0; j < 10; j++) {
        cout << Num[j] << endl;
    }
    return 0;
}
