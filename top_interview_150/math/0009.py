class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        divisor = 1
        while x // divisor >= 10:
            divisor *= 10
        
        while divisor > 1:
            left_digit = x // divisor % 10
            right_digit = x % 10

            if left_digit != right_digit:
                return False

            x = (x % divisor) // 10
            divisor //= 100

        return True

if __name__ == "__main__":
    x = 121
    ans = Solution().isPalindrome(x)
    print(ans)