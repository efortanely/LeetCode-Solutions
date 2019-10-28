class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        if(nums1.length > nums2.length){
            return intersect(nums2, nums1);
        }
        
        HashMap<Integer, Integer> map = new HashMap<>();
        
        for(int n : nums1){
            int val = map.getOrDefault(n, 0);
            map.put(n, val + 1);
        }
        
        int i = 0;
        for(int n : nums2){
            if(map.containsKey(n)){
                nums1[i++] = n;
                int val = map.get(n) - 1;
                if(val > 0){
                    map.put(n, val);
                }else{
                    map.remove(n);
                }
            }
        }
        
        return Arrays.copyOfRange(nums1, 0, i);
    }
}
