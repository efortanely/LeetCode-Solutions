class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        
        prefix = strs[0]
        for s in strs[1:]:
            prefix = self.prefix(prefix, s)
        return prefix
    
    def prefix(self, str1: str, str2: str) -> str:
        prefix = []
        for i in range(min(len(str1), len(str2))):
            if str1[i] == str2[i]:
                prefix.append(str1[i])
            else:
                break
        return ''.join(prefix)
