#include <iostream>

using namespace std;
int binarySearch(int Arr[], int start, int range, int key);

int main(void)
{
    int arr[] = {1,4,7,8,11,15,17,88,100,1000};
    int lengthArr = sizeof(arr)/sizeof(arr[0]);
    int key = 1000;

    int found = binarySearch(arr, 0, lengthArr, key);
    if (found == -1){
        cout << "Sorry " << key << " is not on the array\n";
    }else{
        cout << key << " located at " << found;
    }

}

int binarySearch(int Arr[], int start, int range, int key)
{
    //int arr[] = {1,4,7,8,11,15,17,88,100,1000};
    while (start <= range){
        int mid = start + (range-start)/2;

        if (Arr[mid] == key){
            return mid;
        }else if(key < Arr[mid]){
            range = mid - 1;
        }else{
            start = mid + 1;
        }
    }
    return -1;
}
