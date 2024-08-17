/**
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */
var canPlaceFlowers = function (flowerbed, n) {
  let inBoundsCheck = (idx) => {
    if (idx < 0 || idx >= flowerbed.length) {
      return 0;
    } else {
      return flowerbed[idx];
    }
  };

  if (n == 0) {
    return true;
  }

  for (let i = 0; i < flowerbed.length; i++) {
    let curr = flowerbed[i];
    if (curr == 1) {
      continue;
    }

    if (inBoundsCheck(i - 1) == 0 && inBoundsCheck(i + 1) == 0) {
      flowerbed[i] = 1;
      n--;
      if (n == 0) {
        return true;
      }
    }
  }

  return false;
};

let flowerbed = [1, 0, 1, 0, 1, 0, 1];
let n = 0;
let ans = canPlaceFlowers(flowerbed, n);
console.log(ans);
