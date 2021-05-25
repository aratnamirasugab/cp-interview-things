//https://codeforces.com/problemset/problem/785/A
#include <bits/stdc++.h>
using namespace std;
#define in cin >>
#define out cout <<
#define FOR(i, k, l) for(int i(k);i<l;i++)
#define Vi vector<int>

int main(void) {
    ios_base::sync_with_stdio(false);
    map<string, int> vals;
    vals["Tetrahedron"] = 4;
    vals["Cube"] = 6;
    vals["Octahedron"] = 8;
    vals["Dodecahedron"] = 12;
    vals["Icosahedron"] = 20;

    int n=0, res=0;
    in(n);

    FOR(i,0,n) {
        string temp;
        in(temp);
        res += vals[temp];
    }

    out(res);

}