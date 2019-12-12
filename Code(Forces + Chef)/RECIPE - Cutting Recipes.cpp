//https://www.codechef.com/problems/RECIPE

#include <iostream>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    int T;
    cin >> T;

    vector<int> vec;
    vector<int> res;
    int N = 0, number = 0;

    while(T > 0)
    {
        cin >> N;

        for(int i=0;i<N;i++){
            cin >> number;
            vec.push_back(number);
        }

        int lowest = *min_element(vec.begin(), vec.end());

        bool canDevide = true;

        for(int i=0;i<N;i++){
            if(vec[i] % lowest == 0){
                res.push_back(vec[i]/lowest);
            }else{
                canDevide = false;
            }
        }

        if(canDevide == false){
            for(int i=0;i<N;i++){
                cout << vec[i] << " ";
            }
        }else{
            for(int i=0;i<N;i++){
                cout << res[i] << " ";
            }
        }

        vec.clear(); res.clear();
        cout << "\n";
        T--;

    }
}
