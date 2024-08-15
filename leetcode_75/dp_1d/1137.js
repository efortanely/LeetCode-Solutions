/**
 * @param {number} n
 * @return {number}
 */
var tribonacci = function (n) {
  let dp = (n) => {
    if (memo.has(n)) {
      return memo.get(n);
    }

    memo.set(n, dp(n - 3) + dp(n - 2) + dp(n - 1));
    return memo.get(n);
  };

  let memo = new Map([
    [0, 0],
    [1, 1],
    [2, 1],
  ]);
  return dp(n);
};

ans = tribonacci(31);
console.log(ans);
