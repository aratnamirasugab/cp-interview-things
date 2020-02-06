// https://codeforces.com/contest/734/problem/A
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
    string g; in(g);

    int d=0, a=0;
    FOR(i,0,n) {
        if (g[i] == 'D') d++;
        else a++;
    }

    if (d>a) out("Danik");
    else if (a > d) out("Anton");
    else out("Friendship");
}