var twoSum = function(nums, target) {

    for(let i = 0 ; i < nums.length ; i++) {
        for(let j = 0 ; j < nums.length ; j++){
            if(nums[i] + nums[j] === target && i !== j){
                let arr = [i, j];
                return arr;
            }
        }
    }
};

let nums = [2,7,11,15];
let target = 9;

console.log(twoSum(nums, target));


// Runtime: 152 ms, faster than 21.33% of JavaScript online submissions for Two Sum.
// Memory Usage: 34.7 MB, less than 64.46% of JavaScript online submissions for Two Sum.