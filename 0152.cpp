class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int M_max = nums[0];
        int M_min = nums[0];
        int max_val = nums[0];
        for(int i = 1; i < nums.size(); i++){
            int temp = M_max;
            M_max = max(max(M_max * nums[i], M_min * nums[i]), nums[i]);
            M_min = min(min(temp * nums[i], M_min * nums[i]), nums[i]);
            max_val = max(max(max_val, M_max), M_min);
        }
        return max_val;
    }
};
