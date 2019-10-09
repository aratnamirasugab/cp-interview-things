/*
    Given an unsorted array A of size N of non-negative integers,
    find a continuous sub-array which adds to a given number S.
    https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0
*/

#include <iostream>

using namespace std;

int main(void)
{
    int T;
    cin >> T;

    while(T > 0){
        int N, S;
        cin >> N >> S;
        long long arr[N];

        for(int i = 0 ; i < N ; i++){
            cin >> arr[i];
        }

        int sum [3] = {};
        int tempSum = 0;
        bool set = false;

        for(int i = 0 ; i < N ; i++){
            tempSum = 0;
            for(int j = i ; j < N ; j++){
                if (tempSum == S && set == false){
                    sum[0] = i+1;
                    sum[1] = j;
                    set = true;
                }else{
                    tempSum += arr[j];
                }
            }
        }

        if (set == true){
            cout << sum[0] << " " << sum[1] << "\n";
        }else{
            cout << -1;
        }
        T--;
    }
}
