class Solution{
    public int[] productExceptSelf(int[] nums){
        int[] M1 = new int[nums.length];
        int[] M2 = new int[nums.length + 1];
        int[] nums2 = new int[nums.length];
        M2[nums.length] = 1;

        for(int i = 0; i < nums.length; i++){
            int left = i == 0? 1 : M1[i-1];
            M1[i] = left * nums[i];
        }
            
        for(int i = nums.length - 1; i >= 0; i--){
            int right = i == nums.length - 1? 1 : M2[i+1]; 
            M2[i] = right * nums[i];
        }
        
        for(int i = 0; i < nums.length; i++){
            int left = i == 0? 1 : M1[i-1];
            nums2[i] = left * M2[i+1];
        }
              
        return nums2;
    }
}
