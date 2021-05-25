// https://www.codechef.com/problems/SMPAIR

#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    int arr[100000+5];
    int N, number = 0;
    int T = 0;
    cin >> T;
    while(T > 0){
        cin >> N;
        for(int i = 1 ; i <= N ; i++){
            cin >> number;
            arr[i] = number;
        }
        sort(arr+1, arr + N + 1);
        cout << arr[1] + arr[2] << "\n";
        T--;
    }
}
