class Solution:
    def reverse(self, x: int) -> int:
        seen_zero = True
        minus = False
        num = ''
        for i in reversed(str(x)):
            if i != '0' and len(num) == 0:
                seen_zero = False
            if i == '-':
                minus = True
            if not seen_zero and not minus:
                num += i
        
        if num and int(num) <= pow(2, 31) - 1 and int(num) >= pow(2, 31) * -1:
            return int(num) if not minus else int(num) * -1
        else:
            return 0
