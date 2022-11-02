#include <iostream>
using namespace std;

int arr[26];

int main() {
    char str1[1002], str2[1002];
    cin >> str1;
    cin >> str2;
    int i = 0, j = 0, result = 0;
    while (str1[i]) {
        arr[(int)str1[i] - 'a'] += 1;
        i += 1;
    }
    while (str2[j]) {
        arr[(int)str2[j] - 'a'] -= 1;
        j += 1;
    }
    for (int k = 0; k < 26; ++k) {
        if (arr[k] > 0) {
            result += arr[k];
        } else if (arr[k] < 0) {
            result -= arr[k];
        }
    }

    cout << result << endl;
    return 0;
}