#include<iostream>
#include<bits/stdc++.h>

using namespace std;
int alphaNum[26] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
map<string, int> Alphabet;

int main() {
    string tmp = "abcdefghijklmnopqrstuvwxyz";
    for (int i=0; i < 26; i++) {
        string tmp2;
        tmp2 = tmp[i];
        Alphabet.insert({tmp2, i});
    }
    string word;
    cin >> word;
    int wordLength = word.length();
    for (int j = 0; j < wordLength; j++) {
        string tmp3 = "";
        tmp3 = word[j];
        int tmp4 = Alphabet[tmp3];
        alphaNum[tmp4] += 1;
    }
    for (int k = 0; k < 26; k++) {
        cout << alphaNum[k] << ' ';
    }
    return 0;
}
