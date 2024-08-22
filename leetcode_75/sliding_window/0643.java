class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int sum = 0;
        double maxAvg = Integer.MIN_VALUE;

        for(int i = 0; i < k; i++){
            sum += nums[i];
        }

        maxAvg = Math.max(maxAvg, (double) sum / k);

        for(int i = k; i < nums.length; i++){
            sum -= nums[i-k];
            sum += nums[i];
            maxAvg = Math.max(maxAvg, (double) sum / k);
        }

        return maxAvg;
    }
}