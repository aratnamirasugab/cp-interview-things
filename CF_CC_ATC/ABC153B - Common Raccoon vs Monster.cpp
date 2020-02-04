// https://atcoder.jp/contests/abc153/tasks/abc153_b
#include <bits/stdc++.h>
#define in cin >> 
#define out cout <<
#define Vi vector<int>
#define FOR(i,k,l) for(int i(k); i<l;i++)
#define M 100002

using namespace std;

int main(void) {
    int H, N;
    Vi vec(M);
    cin >> H >> N;
    
    FOR(i,0,N) {
        in(vec[i]);
    }

    int total = 0;
    
    FOR(i,0,N) {
        total += vec[i];
    }

    if (total >= H) out("Yes");
    else out("No");
}