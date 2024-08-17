/**
 * @param {string} s
 * @return {string}
 */
var reverseVowels = function (s) {
  let s_arr = [...s];
  let indexes = [];
  let vowels = [];

  for (let i = 0; i < s_arr.length; i++) {
    if (/[aeiou]/i.test(s_arr[i])) {
      vowels.push(s_arr[i]);
      indexes.push(i);
    }
  }

  for (let index of indexes) {
    s_arr[index] = vowels.pop();
  }

  return s_arr.join("");
};

let s = "aA";
let ans = reverseVowels(s);
console.log(ans);
