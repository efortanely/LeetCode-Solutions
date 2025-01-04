class Solution {
    public int maxSubArray(int[] nums) {
        int max_val = Integer.MIN_VALUE;
        int prev_val = 0;
        //Case 1: Insert the value in the subarray
        //Case 2: Start a new subarray at the value
        for(int i=0; i < nums.length; i++){
            prev_val = Math.max(prev_val + nums[i], nums[i]);
            max_val = Math.max(max_val, prev_val);
        }
        return max_val;
    }
}

