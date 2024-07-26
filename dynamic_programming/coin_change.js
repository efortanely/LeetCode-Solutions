/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function(coins, amount) {
    let memo = new Array(amount + 1).fill(-1);

    let dp = i => {
        if(i > amount){
            return Infinity;
        }
        if(i === amount){
            return 0;
        }
        if(memo[i] !== -1){
            return memo[i];
        }

        let min_amount = Infinity;
        for(let j = 0; j < coins.length; j++){
            let next = 1 + dp(i + coins[j]);
            min_amount = Math.min(min_amount, next);
        }

        memo[i] = min_amount;
        return memo[i];
    }

    let ans = dp(0);
    return ans === Infinity? -1 : ans;
};

let coins = [1,2,5];
let amount = 3;
let ans = coinChange(coins, amount);
console.log(ans);