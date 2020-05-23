class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans =''
        for i in range(len(s)):
            pals = []
            for j in range(i, len(s)+1):
                if s[i:j] == s[i:j][::-1]:
                    pals.append(s[i:j])
            if pals:
                for j in range(len(pals)):
                    if len(pals[j]) > len(ans):
                        ans = pals[j]
        return ans
