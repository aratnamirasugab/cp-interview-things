// function solve(nums, k) {
    
//     let res = false;

//     for (let i = 0 ; i < nums.length ; i++) {
//         let comp = Math.abs(nums[i] - k);
//         let res = nums.includes(comp) && nums[i] !== comp ? true : false;
//         if (res) return true;
//     }
    
//     return res;
// }

// let nums = [35, 8, 18, 3, 22];
// let k = 11;


// const result = solve(nums, k);
// console.log(result);

// ^ dat approach not working when we have array nums like this [45, 1] , k = 44

function solve (nums, k) {
    
    let mep = new Map();

    for (let i = 0 ; i < nums.length ; i++) {
        if (!mep.get(k - nums[i])) {
            return true;
        } else {
            mep.set(nums[i]);
        }
    }

    return false;

}
let nums = [45, 1];
let k = 44;

const result = solve(nums, k);
console.log(result);


