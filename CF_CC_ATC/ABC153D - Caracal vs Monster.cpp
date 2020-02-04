//https://atcoder.jp/contests/abc153/tasks/abc153_d
#include <bits/stdc++.h>
#define in cin >> 
#define out cout <<
#define Vi vector<long int>
#define FOR(i,k,l) for(int i(k); i<l;i++)
#define M 100002
#define heck unsigned long long int

using namespace std;

heck rec(heck H) {
    if (H == 1) return 1;
    else {
        return 2 * rec(H/2) + 1;
    }
}

int main(void) {
    heck H = 0;
    in(H);
    
    out(rec(H));
}
