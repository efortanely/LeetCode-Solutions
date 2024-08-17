/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
var kidsWithCandies = function (candies, extraCandies) {
  let maxCandies = Math.max(...candies);
  let ans = [];

  for (let candy of candies) {
    if (candy + extraCandies >= maxCandies) {
      ans.push(true);
    } else {
      ans.push(false);
    }
  }

  return ans;
};

let candies = [2, 3, 5, 1, 3];
let extraCandies = 3;
ans = kidsWithCandies(candies, extraCandies);
console.log(ans);
