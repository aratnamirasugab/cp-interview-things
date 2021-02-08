/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

// q : https://leetcode.com/problems/two-sum

/**
First approach -- brute force O(n^2)

have 2 pointer, 1st pointer appoint to the lowest index, 2nd pointer points to highest index
let the 2 pointer traverse to meet each other while check if the value sum of the index is equal to target and index is not the same then return both index. If not, then keep traversing to meet each other
*/


/*
Second approach -- Hashmap  time complexity : O(n) space : O(n)

my second approach using hashmap, first we initiate the map and fill it key/value pairs from the nums array, the we traverse the nums array for the second time to check if the target number subtract with the current value on array nums is exist in the map key, if exist then we need to check if the value on the selected key in map is not the same as current index loop on array nums.
*/

// var twoSum = function(nums, target) {
//     let tempMap = new Map();
    
//     for (let i = 0 ; i < nums.length; i++) {
//         tempMap.set(nums[i], i);
//     }
    
//      for (let i = 0 ; i < nums.length; i++) {
//         let complement = target - nums[i];
//         if (tempMap.has(complement) && tempMap.get(complement) !== i) {
//             return [i, tempMap.get(complement)]
//         }
//     }
// };

var twoSum = function(nums, target) {
    let tempMap = new Map();
    
    for (let i = 0 ; i < nums.length ; i++) {
        let complement = target - nums[i];
        if (tempMap.has(complement)) {
            return [tempMap.get(complement), i]
        }
        tempMap.set(nums[i], i);
    }
}