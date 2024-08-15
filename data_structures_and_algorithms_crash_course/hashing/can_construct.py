from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char_counts = Counter(magazine)

        for ch in ransomNote:
            if ch in char_counts:
                char_counts[ch] -= 1
                if char_counts[ch] < 0:
                    return False
            else:
                return False
        
        return True
        
def main():
    runner = Solution()

    ransomNote = "aa"
    magazine = "ab"
    ans = runner.canConstruct(ransomNote, magazine)
    print(ans)

if __name__ == "__main__":
    main()