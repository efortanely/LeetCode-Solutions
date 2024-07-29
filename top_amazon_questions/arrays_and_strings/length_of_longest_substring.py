class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = ans = 0
        n = len(s)

        for right in range(n):
            if len(set(s[left:right+1])) != right - left + 1:
                left += 1
            ans = max(ans, right - left + 1)
        
        return ans

def main():
    runner = Solution()
    s = "au"
    ans = runner.lengthOfLongestSubstring(s)
    print(ans)

if __name__ == "__main__":
    main()