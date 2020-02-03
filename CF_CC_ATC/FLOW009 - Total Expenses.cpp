//https://www.codechef.com/problems/FLOW009

#include <bits/stdc++.h>
#include <iostream>
#include <limits>

using namespace std;

int main(void)
{
    float T, quantity, price;
    cin >> T;

    while(T>0){
    cin >> quantity >> price;

    if(quantity > 1000){
        cout << fixed << setprecision(6) << quantity*price*0.9 << "\n";
    }else{
        cout << fixed << setprecision(6) << quantity*price << "\n";
    }
    T--;
    }
}
