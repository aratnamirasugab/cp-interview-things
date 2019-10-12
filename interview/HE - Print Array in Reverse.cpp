// link https://www.hackerearth.com/practice/data-structures/arrays/1-d/tutorial/

#include <iostream>
using namespace std;

int main(void)
{
    int n;
    cin >> n;

    int arr[n];
    for(int i=0;i<n;i++){
        cin >> arr[i];
    }

    for(int i=n-1;i>=0;i--){
        cout << arr[i] << "\n";
    }
}
