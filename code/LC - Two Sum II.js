/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */

// question : https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
// var twoSum = function(numbers, target) {
//     let tempMap = new Map();
    
//     for (let i = 0 ; i < numbers.length ; i++) {
//         tempMap.set(numbers[i], i);
//     }
    
//     for (let i = 0 ; i < numbers.length ; i++) {
//         let subtraction = target - numbers[i];
//         if (tempMap.has(subtraction) && tempMap.get(subtraction) !== i && i < tempMap.get(subtraction)) {
//             return [i+1, tempMap.get(subtraction)+1]    
//         }
//     }
    
// };

// //

// Solution 2 using two pointer

var twoSum = function(numbers, target) {
    let p1 = 0;
    let p2 = numbers.length - 1;
    
    while (numbers[p1] + numbers[p2] !== target) {
        if (numbers[p1] + numbers[p2] > target) p2--;
        else p1++;
    }
    
    return [p1+1, p2+1];
    
    
}