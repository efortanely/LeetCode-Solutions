from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        i = 0
        j = len(s) - 1

        while i < j:
            second_swap_char = s[i]
            s[i] = s[j]
            s[j] = second_swap_char
            i += 1
            j -= 1
    
def main():
    runner = Solution()

    testcase = ["h","e","l","l","o"]
    runner.reverseString(testcase)
    print(testcase)

if __name__ == "__main__":
    main()