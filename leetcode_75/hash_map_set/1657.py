class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        c1 = Counter(word1)
        c2 = Counter(word2)

        return sorted(c1.keys()) == sorted(c2.keys()) and sorted(c1.values()) == sorted(c2.values())