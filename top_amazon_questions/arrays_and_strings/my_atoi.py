import re

class Solution:
    def myAtoi(self, s: str) -> int:
        match = re.search(r'^[ ]*([-+])?[0]*([0-9]+)', s)
        ans = 0
        if match:
            sign = -1 if match.group(1) == "-" else 1
            num = int(match.group(2))
            ans = sign * num

            if ans < (-2)**31:
                ans = (-2)**31
            if ans > 2**31 - 1:
                ans = 2**31 - 1

            return ans
        
        return ans
        
def main():
    runner = Solution()
    s = "-91283472332"
    ans = runner.myAtoi(s)
    print(ans)

if __name__ == "__main__":
    main()