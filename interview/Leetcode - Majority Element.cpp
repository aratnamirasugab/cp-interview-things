class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int size = nums.size();
        int flag = nums[0];
        int n = 1;

        for(int i = 1 ; i < size ; i++){
            if (n == 0){
                flag = nums[i]; n++;
            }else if(flag == nums[i]){
                n++;
            }else{
                n--;
            }
        }

        return flag;
    }
};
