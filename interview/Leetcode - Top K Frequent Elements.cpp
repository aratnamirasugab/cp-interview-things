#include <vector>
#include <stack>
#include <algorithm>

class Solution {
public:

    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> vec;
        sort(nums.begin(), nums.end());
        int temp = nums[0];

        vec.push_back(temp);
        k--;

        for(int i = 1 ; i < nums.size() ; i++){
            if (temp != nums[i] && k > 0){
                temp = nums[i];
                vec.push_back(temp);
                k--;
            }
        }

        return vec;
    }
};
