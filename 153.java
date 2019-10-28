class Solution {
    public int findMin(int[] nums) {
        if(nums.length == 1){
            return nums[0];
        }
        
        int k = nums.length / 2;
        int[] left = Arrays.copyOfRange(nums, 0, k);
        int[] right = Arrays.copyOfRange(nums, k, nums.length);
        
        if(left.length == 0 || left[left.length-1] > right[right.length-1]){
            return findMin(right);
        }else{
            return findMin(left);
        }
    }
}
