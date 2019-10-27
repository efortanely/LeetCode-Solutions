class Solution {
    public int maxProfit(int[] prices) {
        int max_val = 0;
        int profit = 0;
        if(prices.length == 0){
            return profit;
        }
        
        for(int i = prices.length - 1; i >= 0; i--){
            max_val = Math.max(max_val, prices[i]);
            int new_profit = max_val - prices[i];
            if(new_profit > profit){
                profit = new_profit;
            }
        }
        return profit;
    }
}
