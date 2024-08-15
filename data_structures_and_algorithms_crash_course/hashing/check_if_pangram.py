from typing import List

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        sent = set(sentence)
        return len(sent) == 26
        
def main():
    runner = Solution()

    sentence = "thequickbrownfoxjumpsoverthelazydog"
    ans = runner.checkIfPangram(sentence)
    print(ans)

if __name__ == "__main__":
    main()