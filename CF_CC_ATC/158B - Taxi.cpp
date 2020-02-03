// https://codeforces.com/problemset/problem/158/B
#include <bits/stdc++.h>
#define in cin >>
#define out cout <<
#define Vi vector<int>
#define FOR(i,k,l) for(int i(k); i<l;i++)
#define M 100002

using namespace std;

int main(void) {

    int n, total_taxi = 0;
    in(n);
    Vi vec(M);

    FOR(i,0,n) {
        in(vec[i]);
    }

    sort(vec.begin(), vec.end());
    
    int i=vec.size()-1;
    int k = 0;

    while (k != i) {
        if (vec[i] + vec[k] <=4) {
            vec[i] += vec[k];
            k++;
        }else{
            i--;
            total_taxi++;
        }
    }

    out(total_taxi+1);
}