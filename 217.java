class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> nums2 = new HashSet<>();
        for(int i = 0; i < nums.length; i++){
            if(nums2.contains(nums[i])){
                return true;
            }
            nums2.add(nums[i]);
        }
        return false;
    }
}
