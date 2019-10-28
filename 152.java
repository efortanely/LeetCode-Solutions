class Solution {
    public int maxProduct(int[] nums) {
        int M_max = nums[0];
        int M_min = nums[0];
        int max_val = nums[0];
        for(int i = 1; i < nums.length; i++){
            int temp = M_max;
            M_max = Math.max(Math.max(M_max * nums[i], M_min * nums[i]), nums[i]);
            M_min = Math.min(Math.min(temp * nums[i], M_min * nums[i]), nums[i]);
            max_val = Math.max(Math.max(max_val, M_max), M_min);
        }
        return max_val;
    }
}
