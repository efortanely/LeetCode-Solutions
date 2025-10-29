class Solution:
    def isHappy(self, n: int) -> bool:
        saved_nums = set()
        output = 0

        while output != 1:
            output = 0
            divisor = 1
            while n // divisor >= 10:
                divisor *= 10

            while n > 0:
                left_digit = n // divisor % 10
                output += left_digit**2
                n = n - (left_digit * divisor)
                divisor //= 10

            n = output

            if n in saved_nums:
                return False
            
            saved_nums.add(n)
            
        return True

if __name__ == "__main__":
    n = 19
    ans = Solution().isHappy(n)
    print(ans)
    n = 2
    ans = Solution().isHappy(n)
    print(ans)