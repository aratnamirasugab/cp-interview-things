//https://codeforces.com/problemset/problem/1097/A
#include <bits/stdc++.h>
using namespace std;
#define in cin >>
#define out cout <<
#define FOR(i, k, l) for(int i(k);i<l;i++)
#define Vi vector<int>
#define Msi map<string, int>
#define Mii map<int, int>

int main(void) {
    ios_base::sync_with_stdio(false);
    string n; in(n);

    int res=0;
    FOR(i,0,5) {
        string temp; in(temp);
        if (temp[0] == n[0] || temp[1] == n[1]) res++;
    }

    if(res!= 0) out("YES");
    else out("NO");
}