class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = bin(int(a, 2) + int(b, 2))
        return str(c[2:])
