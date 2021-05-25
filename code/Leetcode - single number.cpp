// https://leetcode.com/problems/single-number/

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int length = nums.size();
        int flag = nums[0];

        for(int i = 1 ; i < length ; i++){
            flag = flag ^ nums[i];
        }

        return flag;
    }
};
