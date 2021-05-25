// Intuition
// store array elements in map
// check if key exist if yes increment value, if not store the key
// get the highest value on map
// 
// Implementation
// I am using map to store the elements in array nums as key so and then if those elements is not present in hashtable/map we store it key and value of 1, if the elements exist, increment the value.
// 
// Time Complexity
// \mathcal{O}(n)O(n) Because we are traversing array from index 0 to N
// 
// Space Complexity
// \mathcal{O}(n)O(n) we store each N element into map

class Solution {
    solve(nums) {
        // store array elements in map
        // check if key exist, if not store key and increment value
        // get the highest value on map

        let mep = new Map();
        if (nums.length === 0) return 0;

        for (let i = 0; i < nums.length; i++) {
            if (!mep.has(nums[i])) mep.set(nums[i], 1);
            else {
                let val = mep.get(nums[i]);
                val += 1;
                mep.set(nums[i], val);
            }
        }

        return Math.max(...mep.values());
    }
}