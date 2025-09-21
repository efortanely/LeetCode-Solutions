from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = Counter(s)
        t = Counter(t)
            
        return s == t

if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    ans = Solution().isAnagram(s, t)
    assert ans == True