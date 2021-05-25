//https://atcoder.jp/contests/abc153/tasks/abc153_c
#include <bits/stdc++.h>
#define in cin >> 
#define out cout <<
#define Vi vector<long int>
#define FOR(i,k,l) for(int i(k); i<l;i++)
#define M 100002

using namespace std;

int main(void) {
    int N, K;
    cin >> N >> K;
    
    vector <long> vec;
    long temp;
    for(int i = 0 ; i < N ; i++) {
        cin >> temp;
        vec.push_back(temp);
    }

    sort(vec.begin(), vec.end());

    unsigned long res = 0;
    for(int i = 0 ; i < N-K ; i++) {
        res += vec[i];
    }

    cout << res << " ";

}