class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = 0
        n2 = 0
        mult = 1
        for i in range(len(num1)-1, -1, -1):
            n1 += mult * int(num1[i])
            mult *= 10
            
        mult = 1
        for i in range(len(num2)-1, -1, -1):
            n2 += mult * int(num2[i])
            mult *= 10
            
        return str(n1 * n2)
