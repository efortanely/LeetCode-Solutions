class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_map = {"2": ["a", "b", "c"],
                     "3": ["d", "e", "f"],
                     "4": ["g", "h", "i"],
                     "5": ["j", "k", "l"],
                     "6": ["m", "n", "o"],
                     "7": ["p", "q", "r", "s"],
                     "8": ["t", "u", "v"],
                     "9": ["w", "x", "y", "z"]}
        
        def helper(combination: str, next_digits: List[str]):
            if len(next_digits) == 0:
                output.append(combination)
            else:
                for letter in phone_map[next_digits[0]]:
                    helper(combination + letter, next_digits[1:])
                
        output = []
        if digits:
            helper("", digits)
        return output
