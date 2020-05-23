class Solution:
    '''
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
    '''
    
    def isMatch(self, s: str, p: str) -> bool:
        M = [[False for c in range(len(p)+1)] for r in range(len(s)+1)]
        M[-1][-1] = True
        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                first_ch = i < len(s) and (p[j] == '.' or p[j] == s[i])
    
                #Case 1: Ignore the wildcard and skip the pattern
                #Case 2: Keep the wildcard and continue using the pattern
                if j+1 < len(p) and p[j + 1] is '*':
                    M[i][j] = M[i][j+2] or (first_ch and M[i+1][j])
                #Case 3: Use the single c/. value
                else:
                    M[i][j] = first_ch and M[i+1][j+1]
        return M[0][0]
            
