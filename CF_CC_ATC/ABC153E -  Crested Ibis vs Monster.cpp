//https://atcoder.jp/contests/abc153/tasks/abc153_e
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll INF = 1e9;
const ll maxh = 5e4 + 10;
const ll maxn = 1010;
ll p[maxn], c[maxn];
ll dp[maxh];

int main()
{
    ll n, h;
    scanf("%lld%lld", &h, &n);
    for(ll i = 0; i < n; i++) scanf("%lld%lld", &p[i], &c[i]);
    fill(dp, dp +  maxh, INF);
    dp[0] = 0;
    for(ll i = 0; i < n; i++) {
        for(ll j = 0; j <= h; j++) {
            dp[j + p[i]] = min(dp[j + p[i]], dp[j] + c[i]);
        }
    }
    ll mins = INF;
    for (ll i = h; i < maxh; i++) mins = min(mins, dp[i]);
    printf("%lld\n", mins);
    return 0;
}