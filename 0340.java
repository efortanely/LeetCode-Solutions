class Solution {
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        int start = 0;
        int maxlen = 0;
        HashMap<Character, Integer> dic = new HashMap<>();
        
        for(int end = 0; end < s.length(); end++){
            char c = s.charAt(end);
            
            //update dictionary counts
            if(dic.containsKey(c)){
                dic.put(c, dic.get(c) + 1);
            }else{
                dic.put(c, 1);
            }
            
            //if dictionary size is larger than k, 
            //update start pointer and dictionary
            while(dic.size() > k){
                c = s.charAt(start);
                dic.put(c, dic.get(c) - 1);
                if(dic.get(c) == 0){
                    dic.remove(c);
                }
                start += 1;
            }
            maxlen = Math.max(maxlen, end - start + 1);
        }
        
        return maxlen;
    }
}
