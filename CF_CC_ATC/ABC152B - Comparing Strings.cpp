#include <bits/stdc++.h>
using namespace std;
#define in cin >>
#define out cout <<
#define FOR(i,k,l) for(int i(k);i<l ; i++)

int main(void) {
    int a, b;
    in(a); in(b);

    if (a < b) {
        FOR(i, 0, b) out(a);
    } else {
        FOR(i, 0, a) out(b);
    }
    cout << "\n";

}