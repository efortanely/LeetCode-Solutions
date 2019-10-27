class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max_val = 0;
        int profit = 0;
        if(prices.size() == 0){
            return profit;
        }
        
        for(int i = prices.size() - 1; i >= 0; i--){
            max_val = max(max_val, prices[i]);
            int new_profit = max_val - prices[i];
            if(new_profit > profit){
                profit = new_profit;
            }
        }
        return profit;
    }
};
