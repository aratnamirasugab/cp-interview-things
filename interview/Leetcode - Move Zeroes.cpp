// https://leetcode.com/problems/move-zeroes/
Runtime: 16 ms, faster than 61.93% of C++ online submissions for Move Zeroes.
Memory Usage: 9.5 MB, less than 86.11% of C++ online submissions for Move Zeroes.

class Solution {
public:
    void moveZeroes(vector<int>& nums) {

        int front = 0;
        int end = 1;

        while(end < nums.size()){
            if (nums[front] == 0 && nums[end] == 0){
                end++;
            }else if (nums[front] == 0 && nums[end] != 0){
                swap(nums[front], nums[end]);
                front++;
            }else if(nums[front] != 0){
                front++;
                end++;
            }
        }
    }
};
