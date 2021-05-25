//https://codeforces.com/problemset/problem/935/A
#include <bits/stdc++.h>
using namespace std;
#define in cin >>
#define out cout <<
#define FOR(i, k, l) for(int i(k);i<l;i++)
#define Vi vector<int>
#define Msi map<string, int>
#define Mii map<int, int>

int main(void) {
    int n; in(n);
    
    int res = 0;
    if (n >= 2) {
        int temp=0;
        FOR(i, 1, n) {
            temp = n - i;
            if (temp % i == 0) res++;
        }
    }

    out(res);

}