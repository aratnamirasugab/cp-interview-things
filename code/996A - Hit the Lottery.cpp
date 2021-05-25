//https://codeforces.com/problemset/problem/996/A   
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
    long n; in(n);
    long res = 0;
    
    Vi vec;
    vec.push_back(1);
    vec.push_back(5);
    vec.push_back(10);
    vec.push_back(20);
    vec.push_back(100);
    sort(vec.begin(), vec.end(), greater<int>());

    int lastIndex = 0;
    while(n > 0) {
        if (n - vec[lastIndex] < 0) lastIndex++;
        else {
            n -= vec[lastIndex];
            res++;
        }
    }

    out(res);
}

// another smart solution
#include <bits/stdc++.h>
using namespace std;
const int MAXN = 105;
int n, ans;
int main()
{
    scanf("%d", &n);
    ans += n/100; n = n%100;
    ans += n/20; n = n%20;
    ans += n/10; n = n%10;
    ans += n/5; n = n%5;
    ans += n;
    printf("%d\n", ans);
    return 0;
}