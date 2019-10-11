#include <iostream>
#include <algorithm>
using namespace std;

//question link : https://practice.geeksforgeeks.org/problems/kadanes-algorithm/0/?track=md-arrays&batchId=144
//using brute force solution would be O(n^2), hence the solution is using the Kadane's algorithm.
//https://www.youtube.com/watch?v=86CQq3pKSUw

/*
    create 2 variable that named max_global and max_local, compare it, if max_local > max_global then change the value
    max_global with max_local

    //this is the pseudocode

    arr[] = [-2,3,2,-1]

    function(int arr[])
        max_global = max_local = arr[0]
        for i start from 1 to length of arr-1
            max_local = max(arr[i], max_local + arr[i])
            if max_local > max_global
                max_global = max_local
        return max_global


    the solution above using Kadane's algo will have time complexity of O(n).
*/

int kadane(int arr[], int n)
{
    int max_local = arr[0];
    int max_global = arr[0];
    for(int i = 1 ; i < n ; i++)
    {
        max_local = max(arr[i], max_local + arr[i]);
        max_global = max(max_local, max_global);
    }

    return max_global;
}

int main(void)
{
    int T;
    cin >> T;

    while(T > 0){

        int n;
        cin >> n;

        int arr[n];

        for(int i = 0 ; i < n ; i++){
            cin >> arr[i];
        }

        int res = kadane(arr, n);
        cout << res;

        T--;
    }
}
