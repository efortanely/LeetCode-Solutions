class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] == 9:
            i = -1
            while digits[i] == 9:
                digits[i] = 0
                i -= 1
                if i == -len(digits) - 1:
                    digits = [0] * (len(digits) + 1)
                    break
            digits[i] += 1
        else:
            digits[-1] += 1
        return digits
