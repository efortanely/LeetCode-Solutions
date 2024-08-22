class Solution {
    public int longestOnes(int[] nums, int k) {
        int answer = Integer.MIN_VALUE;
        int currFlipped = 0;
        int left = 0;
        Queue<Integer> zeroIdx = new LinkedList<>();

        for(int right = 0; right < nums.length; right++){
            if(nums[right] == 0){
                zeroIdx.add(right);
                currFlipped++;
            }

            while(currFlipped > k){
                left = zeroIdx.remove() + 1;
                currFlipped--;
            }

            answer = Math.max(answer, right - left + 1);
        }

        return answer;
    }
}