from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans_map = defaultdict(int)
        ans = length = 0
        
        for idx in range(len(s)):
            ch = s[idx]

            ans_map[ch] += 1
            length += 1

            while ans_map[ch] > 1:
                left = s[idx-length+1]
                ans_map[left] -= 1
                
                if ans_map[left] == 0:
                    del ans_map[left]
                
                length -= 1

            ans = max(ans, length)
        
        return ans

    
def main():
    runner = Solution()

    s = "pwwkew"
    ans = runner.lengthOfLongestSubstring(s)
    print(ans)

if __name__ == "__main__":
    main()