/**
 * @param {string} str1
 * @param {string} str2
 * @return {string}
 */
var gcdOfStrings = function (str1, str2) {
  let gcd = "";

  for (let i = 0; i < str1.length; i++) {
    let prefix = str1.slice(0, i + 1);
    if (sDividesT(str1, prefix) && sDividesT(str2, prefix)) {
      if (prefix.length > gcd.length) {
        gcd = prefix;
      }
    }
  }

  for (let i = 0; i < str2.length; i++) {
    let prefix = str2.slice(0, i + 1);
    if (sDividesT(str1, prefix) && sDividesT(str2, prefix)) {
      if (prefix.length > gcd.length) {
        gcd = prefix;
      }
    }
  }

  return gcd;
};

function sDividesT(s, t) {
  if (s.length % t.length != 0) {
    return false;
  }

  return s == t.repeat(s.length / t.length);
}

let word1 = "LEET";
let word2 = "CODE";
ans = gcdOfStrings(word1, word2);
console.log(ans);
