class Solution:
    def isPalindrome(self, s: str) -> bool:
        #replaces all occurences of characters that aren't a-z, 0-9 with ''
        reg = re.compile(r'[^%s]' % (string.ascii_lowercase + string.digits))
        s = reg.sub('', s.lower())
        k = len(s) // 2
        return s[0:k] == s[-1:len(s)-k-1:-1]
