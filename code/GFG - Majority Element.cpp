// Question link : https://practice.geeksforgeeks.org/problems/majority-element/0/?track=md-arrays&batchId=144
// time complexity of below solution is O(n) because of linear conditional

#include <iostream>
#include <vector>

using namespace std;

int main(void)
{
    int T;
    cin >> T;

    while(T > 0){
        int n;
        cin >> n;
        vector<int> vec(n);
        for(int i = 0 ; i < n ; i++){
            cin >> vec[i];
        }

        int index_major = 0;
        int count_major = 1;

        for(int i = 1 ; i < n ; i++){
            if (vec[i] == vec[index_major]){
                count_major++;
            }else{
                count_major--;
            }

            if (count_major == 0){
                index_major = i;
                count_major = 1;
            }
        }

        count_major = 0;
        for(int i = 0 ; i < n ; i++){
            if (vec[i] == vec[index_major]){
                count_major++;
            }
        }

        if(count_major > n/2){
            cout << vec[index_major] << "\n";
        }else{
            cout << "-1" << "\n";
        }

        T--;
    }
}
