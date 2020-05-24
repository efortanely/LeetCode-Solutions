class Solution:
    def two(self, num: int, ones, teens, tens):
        if num < 10:
            return ones[num]
        elif 10 <= num < 20:
            return teens[num]
        else:
            ten = num // 10
            rest = num - ten * 10
            if rest:
                return tens[ten] + " " + ones[rest]
            else:
                return tens[ten]
    
    def three(self, num: int, ones, teens, tens):
        hundred = num // 100
        rest = num - hundred * 100
        if hundred and rest:
            return ones[hundred] + " Hundred " + self.two(rest, ones, teens, tens)
        elif hundred and not rest:
            return ones[hundred] + " Hundred"
        elif not hundred and rest:
            return self.two(rest, ones, teens, tens)
    
    def numberToWords(self, num: int) -> str:
        ones = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
        teens = {10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"}
        tens = {2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"}
        
        billion = num // 1000000000
        million = (num - billion * 1000000000) // 1000000
        thousand = (num - billion * 1000000000 - million * 1000000) // 1000
        rest = (num - billion * 1000000000 - million * 1000000 - thousand * 1000)
        
        ans = []
        
        if billion:
            ans += [self.three(billion, ones, teens, tens) + " Billion"]
        if million:
            ans += [self.three(million, ones, teens, tens) + " Million"]
        if thousand:
            ans += [self.three(thousand, ones, teens, tens) + " Thousand"]
        if rest:
            ans += [self.three(rest, ones, teens, tens)]
        
        return ' '.join(ans) if ans else "Zero"
