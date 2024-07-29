class Solution:
    def intToRoman(self, num: int) -> str:
        count = 10
        map = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40:"XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}
        ans = ""

        while num > 0:
            val = num % count
            first_digit = val // (count // 10)
            if first_digit == 4 or first_digit == 9:
                ans = map[val] + ans
            else:
                new_val = ""
                
                for key in sorted(map.keys(), reverse=True):
                    if key <= val:
                        first_digit = val // (count // 10)
                        if first_digit <= 3:
                            new_val += map[key] * first_digit
                            val -= key * first_digit
                        else:
                            new_val += map[key]
                            val -= key
                    if val <= 0:
                        break

                ans = new_val + ans
            
            num -= num % count
            count *= 10

        return ans
        
def main():
    runner = Solution()
    num = 1994
    ans = runner.intToRoman(num)
    print(ans)

if __name__ == "__main__":
    main()