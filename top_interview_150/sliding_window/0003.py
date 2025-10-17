class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        substr_set = set()
        longest_length = 0

        while right < len(s):
            if s[right] not in substr_set:
                substr_set.add(s[right])
                longest_length = max(longest_length, right - left + 1)
            else:
                while s[right] in substr_set:
                    substr_set.remove(s[left])
                    left += 1
                substr_set.add(s[right])
            
            right += 1

        return longest_length

if __name__ == "__main__":
    s = "abcabcbb"
    ans = Solution().lengthOfLongestSubstring(s)
    print(ans)