class Solution {
public:
    int lengthOfLongestSubstringKDistinct(string s, int k) {
        int start = 0, maxlen = 0;
        unordered_map<char, int> dic;
        
        for(int end = 0; end < s.size(); end++){
            char c = s[end];
            
            //update dictionary counts
            dic[c] = dic.find(c) != dic.end() ? dic[c] + 1 : 1;
            
            //if dictionary size is larger than k, 
            //update start pointer and dictionary
            while(dic.size() > k){
                c = s[start];
                if(--dic[c] == 0){
                    dic.erase(c);
                }
                start++;
            }
            maxlen = max(maxlen, end - start + 1);
        }
        
        return maxlen;
    }
};
