//https://codeforces.com/problemset/problem/122/A
#include <bits/stdc++.h>

using namespace std;

int main(void) {
    int n;
    cin >> n;

    bool res = false;
    int arr[] = {4,7,47,74,44,444,447,474,477,777,774,744};
    int sizeArr = sizeof(arr)/sizeof(arr[0]);
    for (int i = 0 ; i < sizeArr; i++) {
        if (n % arr[i] == 0){
            res = true;
        }
    }

    if (res) {
        cout << "YES\n";
    } else {
        cout << "NO\n";
    }

}