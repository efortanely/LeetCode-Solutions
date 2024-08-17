/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function (word1, word2) {
  let minLength = Math.min(word1.length, word2.length);
  let ans = "";

  for (let i = 0; i < minLength; i++) {
    let char = word1.charAt(i) + word2.charAt(i);
    ans = ans.concat(char);
  }

  if (minLength < word1.length) {
    ans = ans.concat(word1.slice(minLength));
  }
  if (minLength < word2.length) {
    ans = ans.concat(word2.slice(minLength));
  }

  return ans;
};

let word1 = "ab";
let word2 = "pqrs";
ans = mergeAlternately(word1, word2);
console.log(ans);
