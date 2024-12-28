from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = Counter(magazine)
        note_counter = Counter(ransomNote)
        
        for letter, count in note_counter.items():
            if letter not in counter:
                return False
            if count > counter.get(letter):
                return False
            
        return True

if __name__ == "__main__":
    runner = Solution()
    ransomNote = "aa"
    magazine = "aab"
    ans = runner.canConstruct(ransomNote, magazine)
    print(ans)