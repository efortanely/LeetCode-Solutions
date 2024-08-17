/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
  let prefixProduct = [];
  let suffixProduct = [];
  let ans = [];

  for (let i = 0; i < nums.length; i++) {
    let suffixIdx = nums.length - 1 - i;
    prefixProduct.push(
      prefixProduct.length
        ? nums[i] * prefixProduct[prefixProduct.length - 1]
        : nums[i]
    );
    suffixProduct.unshift(
      suffixProduct.length
        ? nums[suffixIdx] * suffixProduct[0]
        : nums[suffixIdx]
    );
  }

  for (let i = 0; i < nums.length; i++) {
    let productBefore = i > 0 ? prefixProduct[i - 1] : 1;
    let productAfter = i < nums.length - 1 ? suffixProduct[i + 1] : 1;
    ans.push(productBefore * productAfter);
  }

  return ans;
};

let nums = [1, 2, 3, 4];
let ans = productExceptSelf(nums);
console.log(ans);
