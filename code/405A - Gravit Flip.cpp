#include <iostream>
#include <bits/stdc++.h>

using namespace std;

void shift(int *numberA, int *numberB)
{
    int temp = *numberA;
    *numberA = *numberB;
    *numberB = temp;
}

int main(void)
{
    int n;
    cin >> n;

    int arr[1000];

    for (int i = 0 ; i < n ; i++) {
        cin >> arr[i];
    }

    for (int i = 0 ; i < n-1 ; i++){
        for(int j = 0 ; j < n-1 ; j++){
            if (arr[j] > arr[j+1]){
                shift(&arr[j], &arr[j+1]);
            }
        }
    }

    for(int i = 0 ; i < n ; i++){
        cout << arr[i] << " ";
    }

}
