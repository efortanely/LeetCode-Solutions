/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function (s) {
  let wordArr = s.trim().split(/\s+/);
  return wordArr.reverse().join(" ");
};

let s = "a good   example";
let ans = reverseWords(s);
console.log(ans);
