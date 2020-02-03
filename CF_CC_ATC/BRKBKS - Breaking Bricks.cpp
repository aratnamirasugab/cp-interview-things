// https://www.codechef.com/JAN20B/problems/BRKBKS
#include <iostream>
#include <algorithm>
#include <bits/stdc++.h>

using namespace std;

int main(void) {
        int T;
        cin >> T;

        while(T > 0) {
            int s, w[3];
            cin >> s >> w[0] >> w[1] >> w[2];
            sort(w, w+3);
            int total = 0;
            int res = 0;
            for (int i = 0 ; i < 3 ; i++) {
                if (total += w[i] > s) {
                    res++; total += w[i];
                } else {
                    total += w[i];
                }
            }

            cout << res << "\n";

            T--;
        }

}
