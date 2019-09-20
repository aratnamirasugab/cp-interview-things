#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    int n;
    int num = 0;
    int prevNum = 0;
    int totalMagnets = 0;
    cin >> n;

    while(n--){
        cin >> num;
        if (prevNum != num){
            totalMagnets++;
            prevNum = num;
        }
    }

    cout << totalMagnets;

}
