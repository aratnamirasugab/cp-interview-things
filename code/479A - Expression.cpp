// https://codeforces.com/problemset/problem/479/A
#include <bits/stdc++.h>
using namespace std;
#define in cin >>
#define out cout <<

int main(void) {
    int a, b, c;
    in(a); in(b); in(c);

    int res = a + b + c;
    res = max(res, a + b * c);
    res = max(res, a * b + c);
    res = max(res, a * b * c);
    res = max(res, a * (b + c));
    res = max(res, (a + b) * c);
    
    out(res);
}