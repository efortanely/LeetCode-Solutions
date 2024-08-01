class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left = right = max_len = 0
        seen = {}

        while right < len(s):
            seen[s[right]] = right

            while len(seen) > 2:
                if seen[s[left]] == left:
                    seen.pop(s[left])
                
                left += 1
        
            max_len = max(max_len, right - left + 1)
            right += 1
        
        return max_len

def main():
    runner = Solution()
    s = "abaccc"
    ans = runner.lengthOfLongestSubstringTwoDistinct(s)
    print(ans)

if __name__ == "__main__":
    main()