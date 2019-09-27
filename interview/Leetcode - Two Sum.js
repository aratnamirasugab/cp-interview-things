var twoSum = function(nums, target) {

    for(let i = 0 ; i < nums.length() ; i++) {
        for(let j = 0 ; j < nums.length() ; j++){
            if(nums[i] + nums[j] === target && i !== j){
                console.log(`[${i, j}]`);
            }
        }
    }
};

let nums = [2,7,11,15];
let target = 9;

twoSum(nums, target);