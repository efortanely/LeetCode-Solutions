/**
 * @param {character[]} chars
 * @return {number}
 */
var compress = function (chars) {
  let left = 0;
  let right = 0;
  let currChar = "";
  let ans = 0;

  while (left < chars.length) {
    currChar = chars[left];

    while (right < chars.length && chars[right] == currChar) {
      right++;
    }

    chars[ans] = currChar;
    ans++;

    let count = right - left;
    if (count > 1) {
      let countStr = String(count);
      for (let c of countStr) {
        chars[ans] = c;
        ans++;
      }
    }

    left = right;
  }

  return ans;
};

let chars = ["a", "a", "b", "b", "c", "c", "c"];
let ans = compress(chars);
console.log(ans);
