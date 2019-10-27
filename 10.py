class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        first_ch = s and (p[0] == '.' or p[0] == s[0])
    
        #Case 1: Ignore the wildcard and skip the pattern
        #Case 2: Keep the wildcard and continue using the pattern
        if len(p) >= 2 and p[1] is '*':
            return self.isMatch(s, p[2:]) or (first_ch and self.isMatch(s[1:], p))
        #Case 3: Use the single c/. value
        else:
            return first_ch and self.isMatch(s[1:], p[1:])
