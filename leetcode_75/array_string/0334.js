/**
 * @param {number[]} nums
 * @return {boolean}
 */
var increasingTriplet = function (nums) {
  let i = Number.MAX_VALUE;
  let j = Number.MAX_VALUE;

  for (let num of nums) {
    if (num <= i) {
      i = num;
    } else if (num <= j) {
      j = num;
    } else {
      return true;
    }
  }

  return false;
};

let nums = [1, 1, -2, 6];
let ans = increasingTriplet(nums);
console.log(ans);
