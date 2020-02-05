//https://codeforces.com/problemset/problem/1030/A
#include <bits/stdc++.h>
using namespace std;
#define in cin >>
#define out cout <<
#define FOR(i, k, l) for(int i(k);i<l;i++)
#define Vi vector<int>

int main(void) {
    int hard = 0;
    int n; in(n);
    int temp = 0;

    FOR(i, 0, n) {
        in(temp);
        if (temp == 1) hard = 1;
    }

    if (hard == 0) out("Easy");
    else out("Hard");


}