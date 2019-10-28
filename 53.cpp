class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int max_val = INT_MIN;
        int prev_val = 0;
        //Case 1: Insert the value in the subarray
        //Case 2: Start a new subarray at the value
        for(int i = 0; i < nums.size(); i++){
            prev_val = max(prev_val + nums[i], nums[i]);
            max_val = max(max_val, prev_val);
        }
        return max_val;
    }
};
