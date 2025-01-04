class Solution:
    def isPalindrome(self, s: str) -> bool:
        regex = re.compile("[\W]")
        s = regex.sub('', s.lower())
        return s == s[::-1]
