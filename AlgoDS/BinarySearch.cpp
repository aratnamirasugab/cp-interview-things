#include <iostream>

using namespace std;

int binarySearch(int arr[], int left, int right, int number)
{
    while(left <= right)
    {
        int mid = (left+right)/2;

        if(arr[mid] == number){
            return mid;
        }

        //if value on mid is less than number to be search
        if(arr[mid] < number){
            left = mid +1;
        }else{
            right = mid -1;
        }

    }
    return -1;
}

int main(void)
{
    int arr[] = {1,2,3,5,88,100};
    int arrSize = sizeof(arr)/sizeof(arr[0]);
    int numberToSearch = 0;
    cin >> numberToSearch;
    int res = binarySearch(arr, 0, arrSize, numberToSearch);
    cout << "number " << numberToSearch << " is located at arr : " << res << " ";
}
