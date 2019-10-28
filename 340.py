class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        start, maxlen = 0, 0
        dic = dict()
        
        for end in range(len(s)):
            c = s[end]
            
            #update dictionary counts
            dic[c] = dic[c] + 1 if c in dic else 1

            #if dictionary size is larger than k, 
            #update start pointer and dictionary
            while(len(dic) > k):
                c = s[start]
                dic[c] -= 1
                if dic[c] == 0:
                    del dic[c]
                start += 1
            
            maxlen = max(maxlen, end - start + 1)
            
        return maxlen
