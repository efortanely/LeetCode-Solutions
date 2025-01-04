class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, "D": 500, "M": 1000}
        left, right = 0, 1
        num = 0
        while left < len(s):
            if right < len(s) and dic[s[left]] < dic[s[right]]:
                num += dic[s[right]] - dic[s[left]]
                left = right + 1
                right = left + 1
            else:
                num += dic[s[left]]
                left += 1
                right += 1
        
        return num
