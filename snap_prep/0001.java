class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> numSet = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            int n1 = nums[i];
            int n2 = target - n1;
            if(numSet.containsKey(n2) == true){
                int j = numSet.get(n2);
                int[] ans = {i,j};
                return ans;
            }
            numSet.put(n1, i);
        }
        return null;
    }
}
