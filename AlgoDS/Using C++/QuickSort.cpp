#include <iostream>
#include <algorithm>

using namespace std;

int partition(int *Arr, int start, int end);
void QuickSort(int *Arr, int start, int end);

int main(void)
{
    int arr[] = {9,8,7,6,4,3,2,1};
    int lengthArr = sizeof(arr)/sizeof(arr[0]);
    for (int i = 0 ; i < lengthArr ; i++){
        cout << arr[i] << " ";
    }

    QuickSort(arr, 0, lengthArr-1);
    cout << "\n";
    for (int i = 0 ; i < lengthArr ; i++){
        cout << arr[i] << " ";
    }

}

int partition(int *Arr, int start, int end)
{
    int index = start;
    int pivot = Arr[end];
    for(int i = start ; i < end ; i++){
        if (Arr[i] <= pivot) {
            swap(Arr[i], Arr[index]);
            index++;
        }
        swap(Arr[pivot], Arr[index]);
    }

    return index;
}

void QuickSort(int *Arr, int start, int end)
{
    if (start < end) {
        int partitionIndex = partition(Arr, start, end);
        QuickSort(Arr, start, partitionIndex-1);
        QuickSort(Arr, partitionIndex+1, end);
    }
}

