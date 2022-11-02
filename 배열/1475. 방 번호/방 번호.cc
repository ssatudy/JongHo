#include<iostream>
#include<bits/stdc++.h>

using namespace std;
int Num[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};


int main() {
    string InputNum;
    cin >> InputNum;
    for (int i = 0; i < InputNum.length(); i++) {
        if (InputNum[i] == '0') {
            Num[0] += 1;
        }
        else if (InputNum[i] == '1') {
            Num[1] += 1;
        }
        else if (InputNum[i] == '2') {
            Num[2] += 1;
        }
        else if (InputNum[i] == '3') {
            Num[3] += 1;
        }
        else if (InputNum[i] == '4') {
            Num[4] += 1;
        }
        else if (InputNum[i] == '5') {
            Num[5] += 1;
        }
        else if (InputNum[i] == '6') {
            if (Num[6] > Num[9]) {
                Num[9] += 1;
            }
            else {
                Num[6] += 1;
            }
        }
        else if (InputNum[i] == '7') {
            Num[7] += 1;
        }
        else if (InputNum[i] == '8') {
            Num[8] += 1;
        }
        else {
            if (Num[6] >= Num[9]) {
                Num[9] += 1;
            }
            else {
                Num[6] += 1;
            }
        }
    }
    int maxV = 0;
    for (int j = 0; j < 10; j++) {
        if (j == 0) {
            maxV = Num[j];
        }
        else {
            if (Num[j] > maxV) {
                maxV = Num[j];
            }
        }
    }
    cout << maxV;
    return 0;
}
