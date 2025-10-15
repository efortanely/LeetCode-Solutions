class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1

        while i >= 0 or j >= 0 or carry:
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0

            total = digit_a + digit_b + carry
            result.append(str(total % 2))
            carry = total // 2

            i -= 1
            j -= 1

        return ''.join(reversed(result))

if __name__ == "__main__":
    a = "101111"
    b = "10"
    ans = Solution().addBinary(a, b)
    print(ans)
    print("exp: " + "110001")