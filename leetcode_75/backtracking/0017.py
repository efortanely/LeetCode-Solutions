from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def backtrack(curr, i):
            if len(curr) == len(digits):
                ans.append("".join(curr[:]))
                return
            
            for j in range(i, len(digits)):
                for alpha in digitMap[digits[j]]:
                    curr.append(alpha)
                    backtrack(curr, j+1)
                    curr.pop()
        
        digitMap = {"2": ["a", "b", "c"], 
                    "3": ["d", "e", "f"],
                    "4": ["g", "h", "i"],
                    "5": ["j", "k", "l"],
                    "6": ["m", "n", "o"],
                    "7": ["p", "q", "r", "s"],
                    "8": ["t", "u", "v"],
                    "9": ["w", "x", "y", "z"]}

        ans = []

        if not digits:
            return ans

        backtrack([], 0)
        return ans

if __name__ == "__main__":
    digits = "23"
    ans = Solution().letterCombinations(digits)
    assert ans == ["ad","ae","af","bd","be","bf","cd","ce","cf"]