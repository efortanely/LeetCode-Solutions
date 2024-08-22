class Solution {
    public int longestSubarray(int[] nums) {
        int answer = Integer.MIN_VALUE;
        int left = 0;
        int zeroIdx = -1;

        for(int right = 0; right < nums.length; right++){
            if(nums[right] == 0){
                left = zeroIdx + 1;
                zeroIdx = right;
            }

            answer = Math.max(answer, right - left);
        }

        return answer;
    }
}