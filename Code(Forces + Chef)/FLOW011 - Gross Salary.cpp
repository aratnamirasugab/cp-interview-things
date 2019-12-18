// https://www.codechef.com/problems/FLOW011

#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    int T = 0;
    cin >> T;

    while(T > 0){

        int salary = 0;
        cin >> salary;

        if(salary < 1500){
            cout << fixed << setprecision(2) << static_cast<float>(salary*2) << "\n";
        }else{

            cout << fixed << setprecision(2) << salary+500 + (0.98 * salary) << "\n";

        }

        T--;
    }
}
