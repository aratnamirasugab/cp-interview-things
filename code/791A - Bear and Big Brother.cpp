// https://codeforces.com/problemset/problem/791/A
#include <bits/stdc++.h>
using namespace std;
#define in cin >>
#define out cout <<
#define FOR(i, k, l) for(int i(k);i<l;i++)
#define Vi vector<int>
#define Msi map<string, int>
#define Mii map<int, int>

int main(void) {
    int a=0, b=0; in(a); in(b);
    int res=0;
    while (a <= b) {
        res++;
        a *= 3; b *= 2;
    }
    out(res);
}