//https://codeforces.com/problemset/problem/977/A

#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    int n=0,k=0;
    cin >> n >> k;

    while(k > 0)
    {
        if(n % 10 != 0) n--;
        else{
            n = n/10;
        }
        k--;
    }

    cout << n << "\n";
}
