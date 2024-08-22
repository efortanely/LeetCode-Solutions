class Solution {
    public void moveZeroes(int[] nums) {
        Queue<Integer> numsSaved = new LinkedList<>();

        for(int i = 0; i < nums.length; i++){
            int element = nums[i];

            if(element != 0){
                numsSaved.add(element);
            }
        }

        for(int i = 0; i < nums.length; i++){
            if(!numsSaved.isEmpty()){
                nums[i] = numsSaved.remove();
            }else{
                nums[i] = 0;
            }
        }
    }
}