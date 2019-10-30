class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set1 = set()
        left = 0
        right = 0
        max_val = 0
        while right < len(s):
            if s[right] not in set1:
                set1.add(s[right])
                right += 1
                max_val = max(max_val, right - left)
            else:
                set1.remove(s[left])
                left += 1
        return max_val
                
