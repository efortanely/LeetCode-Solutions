class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = dict()
        
        for c in s:
            if c in dict1:
                dict1[c] += 1
            else:
                dict1[c] = 1
        
        for c in t:
            if c in dict1 and dict1[c] > 0:
                dict1[c] -= 1
                if dict1[c] is 0:
                    del dict1[c]
            else:
                return False
        
        return len(dict1) == 0
