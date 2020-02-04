// https://codeforces.com/problemset/problem/318/A
#include <bits/stdc++.h>
using namespace std;
#define in cin >>
#define out cout <<
#define FOR(i, k, l) for(int i(k);i<=l;i++)
#define FOR2(i, k, l) for(int i(k);i<=l;i++)
#define vc vector<long long>

int main(void) {
    long long n, k;
    in(n); in(k);

    if (k <= (n+1)/2) out(2*k-1);
    else out((k - (n + 1) / 2) * 2);
}

// old solution using vector, got time limit exceedeed.
// https://codeforces.com/problemset/problem/318/A
#include <bits/stdc++.h>
using namespace std;
#define in cin >>
#define out cout <<
#define FOR(i, k, l) for(int i(k);i<=l;i++)
#define FOR2(i, k, l) for(int i(k);i<=l;i++)
#define vc vector<int>
 
int main(void) {
    int n, k;
    in(n); in(k);
 
    vc resVc;
    FOR(i,1,n) {
        if (i % 2 != 0) resVc.push_back(i);
    }
 
    FOR2(i,1,n) {
        if (i % 2 == 0) resVc.push_back(i);
    }
 
    out(resVc[k-1]);
 
}