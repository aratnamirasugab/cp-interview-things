https://leetcode.com/problems/sort-array-by-parity/

Runtime: 32 ms, faster than 27.52% of C++ online submissions for Sort Array By Parity.
Memory Usage: 10.5 MB, less than 5.17% of C++ online submissions for Sort Array By Parity.

#include <vector>
#include <algorithm>

class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& A) {
        vector<int> res;
        vector<int> even;
        vector<int> odd;

        for(int i = 0 ; i < A.size() ; i++){
            if(A[i] % 2 == 0){
                even.push_back(A[i]);
            }else{
                odd.push_back(A[i]);
            }
        }

        copy(even.begin(), even.end(), back_inserter(res));
        copy(odd.begin(), odd.end(), back_inserter(res));

        return res;
    }
};
