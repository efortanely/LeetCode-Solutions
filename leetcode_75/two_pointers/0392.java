class Solution {
    public boolean isSubsequence(String s, String t) {
        if(s.length() == 0){
            return true;
        }
        
        int sPointer = 0;

        for(char c : t.toCharArray()){
            if(sPointer == s.length()){
                break;
            }else if(c == s.charAt(sPointer)){
                sPointer++;
            }
        }

        return sPointer == s.length() ? true : false;
    }
}