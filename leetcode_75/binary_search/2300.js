/**
 * @param {number[]} spells
 * @param {number[]} potions
 * @param {number} success
 * @return {number[]}
 */
var successfulPairs = function (spells, potions, success) {
  potions = potions.sort((a, b) => a - b);
  let pairs = new Map();
  let ans = [];

  for (let spell of spells) {
    if (pairs.has(spell)) {
      ans.push(pairs.get(spell));
    } else {
      let potionStrength = Math.ceil(success / spell);
      let left = 0;
      let right = potions.length;

      while (left < right) {
        let mid = Math.floor((left + right) / 2);
        let potion = potions[mid];

        if (potion >= potionStrength) {
          right = mid;
        } else {
          left = mid + 1;
        }
      }

      let totalPotions = potions.length - left;
      pairs.set(spell, totalPotions);
      ans.push(totalPotions);
    }
  }

  return ans;
};

let spells = [
  13, 22, 21, 13, 11, 9, 13, 35, 7, 38, 10, 10, 38, 19, 3, 16, 13, 24, 16, 27,
  20, 24, 32, 5, 16, 35, 24, 2, 25, 32, 20, 22, 22, 3, 35, 39, 27, 26, 25, 21,
  27, 40, 15, 17, 24, 40, 35, 27, 20, 40, 9, 35, 27, 19, 15, 34, 35, 37, 17, 40,
  8, 3, 33, 39, 29, 22, 30, 1, 37, 2, 16, 30, 32, 31, 24, 6, 34, 26, 36, 4, 21,
  2, 29, 31, 3, 27, 6, 24, 40, 18,
];
let potions = [
  33, 16, 35, 14, 26, 23, 23, 2, 37, 23, 15, 20, 25, 34, 23, 29, 4, 18, 26, 24,
  16, 37, 15, 11, 33, 24, 12, 13, 7, 24, 3, 26, 1, 3, 38, 33, 19, 3, 34, 22, 30,
  39, 18, 7, 21, 4, 33, 18, 39, 5, 34, 14, 32, 5, 20, 22, 5, 25, 15,
];
let success = 533;
let ans = successfulPairs(spells, potions, success);
console.log(ans);
