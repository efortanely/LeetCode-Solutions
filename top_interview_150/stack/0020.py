class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map_paren = {"(": ")", "{": "}", "[": "]"}
        for x in s:
            if x in ["(", "{", "["]:
                stack.append(x)
            else:
                if stack:
                    last_paren = stack.pop()
                else:
                    return False
                
                if map_paren[last_paren] != x:
                    return False
                
        return not stack

if __name__ == "__main__":
    runner = Solution()
    s = "]"
    ans = runner.isValid(s)
    print(ans)