class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for c in s:
            if stack and ((c.islower() and stack[-1] == c.upper()) or (c.isupper() and stack[-1] == c.lower())):
                stack.pop()
            else:
                stack.append(c)

        return "".join(stack)

def main():
    runner = Solution()

    s = "leEeetcode"
    ans = runner.makeGood(s)
    print(ans)

if __name__ == "__main__":
    main()