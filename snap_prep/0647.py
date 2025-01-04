class Solution:
    def countSubstrings(self, s: str) -> int:
        pal = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if self.isPal(s[i:j]):
                    pal += 1
        return pal
        
    def isPal(self, s: str) -> bool:
        return s == s[::-1]
