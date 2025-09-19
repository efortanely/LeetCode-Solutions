class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for c in s:
            if c != "*":
                stack.append(c)
            else:
                stack.pop()
        
        return "".join(stack)

if __name__ == "__main__":
    runner = Solution()
    s = "leet**cod*e"
    ans = runner.removeStars(s)
    print(ans)