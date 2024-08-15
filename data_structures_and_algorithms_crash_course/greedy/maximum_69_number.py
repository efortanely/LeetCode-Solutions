import math

class Solution:
    def maximum69Number (self, num: int) -> int:
        num_digits = int(math.log10(num)) + 1
        ans = 0
        flipped = False

        for i in range(num_digits, 0, -1):
            divisor = 10**(i-1)
            digit = num // divisor
            num -= digit * divisor
            
            if not flipped and digit == 6:
                digit = 9
                flipped = True
            
            ans += digit * divisor

        return ans

def main():
    runner = Solution()

    num = 9669
    ans = runner.maximum69Number(num)
    print(ans)

if __name__ == "__main__":
    main()