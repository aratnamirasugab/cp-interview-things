//https://codeforces.com/contest/677/problem/A
#include <bits/stdc++.h>
using namespace std;
#define in cin >>
#define out cout <<
#define FOR(i, k, l) for(int i(k);i<l;i++)
#define Vi vector<int>
#define Msi map<string, int>
#define Mii map<int, int>

int main(void) {
    int n, h; in(n); in(h);
    int res=0, temp=0;

    FOR(i, 0, n) {
        in(temp);
        if (temp > h) res += 2;
        else res++;
    }

    out(res);
}