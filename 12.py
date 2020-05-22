class Solution:
    def thousands(self, num: int):
        if num == 0:
            return ''
        elif num == 1:
            return 'M'
        elif num == 2:
            return 'MM'
        elif num == 3:
            return 'MMM'
    
    def hundreds(self, num: int):
        if num == 0:
            return ''
        elif num == 1:
            return 'C'
        elif num == 2:
            return 'CC'
        elif num == 3:
            return 'CCC'
        elif num == 4:
            return 'CD'
        elif num == 5:
            return 'D'
        elif num == 6:
            return 'DC'
        elif num == 7:
            return 'DCC'
        elif num == 8:
            return 'DCCC'
        elif num == 9:
            return 'CM'
    
    def tens(self, num: int):
        if num == 0:
            return ''
        elif num == 1:
            return 'X'
        elif num == 2:
            return 'XX'
        elif num == 3:
            return 'XXX'
        elif num == 4:
            return 'XL'
        elif num == 5:
            return 'L'
        elif num == 6:
            return 'LX'
        elif num == 7:
            return 'LXX'
        elif num == 8:
            return 'LXXX'
        elif num == 9:
            return 'XC'
    
    def digits(self, num: int):
        if num == 0:
            return ''
        elif num == 1:
            return 'I'
        elif num == 2:
            return 'II'
        elif num == 3:
            return 'III'
        elif num == 4:
            return 'IV'
        elif num == 5:
            return 'V'
        elif num == 6:
            return 'VI'
        elif num == 7:
            return 'VII'
        elif num == 8:
            return 'VIII'
        elif num == 9:
            return 'IX'
    
    def intToRoman(self, num: int) -> str:
        ans = ''
        s = str(num)
        if len(s) >= 4:
            ans += self.thousands(int(s[0]))
            s = s[1:]
        if len(s) >= 3:
            ans += self.hundreds(int(s[0]))
            s = s[1:]
        if len(s) >= 2:
            ans += self.tens(int(s[0]))
            s = s[1:]
        if len(s) >= 1:
            ans += self.digits(int(s[0]))
        return ans
