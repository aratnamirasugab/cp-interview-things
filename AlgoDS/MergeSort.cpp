//implementation of MergeSort
//for further information and learning
//link : https://www.youtube.com/watch?v=TzeBrDU-JaY
//wiki : https://en.wikipedia.org/wiki/Merge_sort

//Time complexity of Merge Sort is (n Log n) in all 3 cases (worst, average and best)..
//as merge sort always divides the array into two halves and take linear time to merge two halves.

#include <iostream>
using namespace std;

void mergeArr(int arr[], int left, int mid, int right)
{
    int p = left, q = mid+1;
    int Arr[right-left+1], K = 0;

    for(int i=left;i<right;i++){
        if(p > mid){
            Arr[K++] = arr[q++];
        }else if(q > right){
            Arr[K++] = arr[p++];
        }else if(arr[p] < Arr[p++]){
            Arr[K++] = arr[p++];
        }else{
            Arr[K++] = arr[q++];
        }
    }
    for(int p=0;p<K;p++){
        arr[left++] = Arr[p];
    }
}

int mergeSort(int arr[], int left, int right)
{
    // 0 // 8
    //int arr[] = {9,8,7,6,5,4,3,2,1};

    // LEFT ARRAY

    // 0 // 4
    //arrLeft = {9,8,7,6,5};

    // 0 // 2
    //arrLeft = {9,8,7};

    // 0 // 1
    //arrLeft = {9,8};

    // 0 // 0
    //arrLeft = {9}

    // 1 // 1
    //arrRight = {8};

    //compare and merge arr
    //arr = {8,9};

    // 2 // 2
    //arrRight = {7};

    //compare and merge arr
    //arr = {7,8,9};

    //3 // 4
    //arrLeft = {6}

    //4 // 4
    //arrRight = {5}

    //compare and merge arr
    //arr = {5,6}

    //compare and merge arr
    //arr = {5,6,7,8,9};

    //ARRAY LEFT IS {5,6,7,8,9}

    //ARRAY RIGHT
    //5 // 8
    // {4,3,2,1}

    //5 // 6
    //arrLeft = {4,3}

    //5 // 5
    //arrLeft = {4}

    // 6 // 6
    //arrRight = {3}

    //compare and merge
    // 5 // 6
    //arr = {3,4}

    // 7 // 8
    // arrLeft = {2,1}

    // 7 // 7
    // arrLeft = {2}

    // 8 // 8
    // arrRight = {1}

    // compare and merge
    // arr = {1,2}

    // compare and merge
    // arr = {3,4} ; arr = {1,2}
    // arr = {1,2,3,4}

    //compare and merge BOTH ARRAY
    // arr = {5,6,7,8,9} ; arr = {1,2,3,4}
    // arr = {1,2,3,4,5,6,7,8,9};

    if(left < right){
        int mid = (left+right)/2;

        //sort left
        mergeSort(arr, left, mid);
        //sort right
        mergeSort(arr, mid+1, right);
        //merge both array
        mergeArr(arr, left, mid, right);
    }
}

int main(void)
{
    int arr[] = {9,8,7,6,5,4,3,2,1};
    int arr_size = sizeof(arr)/sizeof(arr[0]);

    mergeSort(arr, 0, arr_size-1);

    for(int i=0;i<arr_size;i++){
        cout << arr[i] << "\n";
    }
}
