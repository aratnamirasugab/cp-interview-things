#include <bits/stdc++.h>
using namespace std;
#define in cin >>
#define out cout <<
#define FOR(i, k, l) for(int i(k);i<l;i++)
#define Vi vector<int>
#define Msi map<string, int>

int main(void) {
    ios_base::sync_with_stdio(false);
    Vi vec;

    FOR(i,0, 4) {
        int temp; in(temp);
        vec.push_back(temp);
    }

    sort(vec.begin(), vec.end());
    int high = vec[3];
    out(abs(high-vec[0]));
    out("\n");
    out(abs(high-vec[1]));
    out("\n");
    out(abs(high-vec[2]));
    
}