from typing import List, Deque

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        reversed_digits = list(reversed(digits))

        curr_digit = reversed_digits[0] + 1
        if curr_digit < 10:
            return digits[:-1] + [curr_digit]
        else:
            ans = Deque([0])
            i = 1
            carry = curr_digit % 9

            while carry:
                if i < len(reversed_digits):
                    curr_digit = reversed_digits[i] + carry
                else:
                    curr_digit = carry
                if curr_digit < 10:
                    ans.appendleft(curr_digit)
                    i += 1
                    break
                ans.appendleft(0)
                carry = curr_digit % 9
                i += 1

            return digits[:-i] + list(ans)
            
if __name__ == "__main__":
    digits = [9,9,9,9]
    ans = Solution().plusOne(digits)
    print(ans)