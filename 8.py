class Solution:
    def myAtoi(self, s: str) -> int:
        matches = re.search("^\s*([+-]?\d+)[\w\s]*", s)
        if matches:
            return max(min(int(matches.group(1)), pow(2, 31) - 1), pow(-2, 31))
        return 0
