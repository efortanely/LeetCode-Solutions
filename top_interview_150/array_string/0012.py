class Solution:
    def intToRoman(self, num: int) -> str:
        div = 1000
        roman_map = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}
        ans = ""

        while num:
            curr = (num // div) * div
            digit = num // div
            
            if curr in roman_map:
                ans += roman_map[curr]
            else:
                if 1 < digit < 4:
                    ans += roman_map[div] * digit
                elif 5 < digit < 9:
                    ans += roman_map[div * 5] + (roman_map[div] * (digit - 5))

            num -= curr
            div //= 10

        return ans

if __name__ == "__main__":
    num = 6
    ans = Solution().intToRoman(num)
    print(ans)