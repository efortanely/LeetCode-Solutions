from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        
        def backtrack(curr, i):
            if i >= len(digits):
                if curr:
                    ans.append(curr)
                return

            for letter in map[digits[i]]:
                curr += letter
                backtrack(curr, i+1)
                curr = curr[:-1]

        ans = []
        backtrack("", 0)
        return ans

def main():
    runner = Solution()
    digits = "2"
    ans = runner.letterCombinations(digits)
    print(ans)

if __name__ == "__main__":
    main()