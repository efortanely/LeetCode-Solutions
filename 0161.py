class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if (t in s and abs(len(s) - len(t)) == 1) or (s in t and abs(len(s) - len(t)) == 1):
            return True
        elif (not s and len(t) == 1) or (not t and len(s) == 1):
            return True
        elif s == t:
            return False
        
        for i in range(len(s)):
            s_cut = s[:i] + s[i+1:]
            t_cut = t[:i] + t[i+1:]
            
            if t_cut == s:
                return True
            elif s_cut == t:
                return True
            elif s_cut == t_cut:
                return True
        return False
