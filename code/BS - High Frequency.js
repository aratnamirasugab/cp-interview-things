class Solution {
    solve(nums) {
        // store array elements in map
        // check if key exist, if not store key and increment value
        // get the highest value on map

        // Time : O(n)
        // Space : O(n)

        let mep = new Map();
        if (nums.length === 0) return 0;

        for (let i = 0 ; i < nums.length ; i++) {
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