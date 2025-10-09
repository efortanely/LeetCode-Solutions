class Solution:
    def romanToInt(self, s: str) -> int:
        conversions = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        special = {"IV", "IX", "XL", "XC", "CD", "CM"}
        ans = 0
        i = 0

        while i < len(s):
            if i < len(s) - 1 and s[i:i+2] in special:
                ans += conversions[s[i+1]] - conversions[s[i]]
                i += 2
            else:
                ans += conversions[s[i]]
                i += 1
        
        return ans

if __name__ == "__main__":
    s = "MCMXCIV"
    ans = Solution().romanToInt(s)
    print(ans)