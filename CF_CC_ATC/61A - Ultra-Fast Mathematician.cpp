// https://codeforces.com/problemset/problem/61/A

#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    vector<int> res;
    int a=0,b=0;
    cin >> a >> b;

    while(a >= 0 || b >= 0){
        if(a % 10 == b % 10){
            res.push_back(0);
        }else{
            res.push_back(1);
        }
        a /= 10; b/=10;
    }

    reverse(res.begin(), res.end());

    for(int i = 0 ; i < res.size(); i++){
        cout << res[i];
    }

}
