#include <bits/stdc++.h>
#include <iostream>
#include <stdbool.h>

using namespace std;

bool isLucky(int n)
{
    if (n % 4 == 0 || n % 7 == 0){
        return true;
    }

    int howManyNumber = 0;
    int howManyLucky = 0;
    while (n > 0){
        int lucky = n % 10;
        howManyNumber++;
        if (lucky == 4 || lucky == 7){
            howManyLucky++;
        }
        n = n / 10;
    }

    if (howManyLucky == howManyNumber){
        return true;
    }
}

int main(void)
{
    int n;
    cin >> n;

    bool res = false;
    res = isLucky(n);
    cout << res;
}
