from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(curr, open_num, close_num):
            if len(curr) == 2 * n:
                ans.append(curr[:])
                return
            
            if open_num < n:
                curr += "("
                backtrack(curr, open_num + 1, close_num)
                curr = curr[:-1]

            if close_num < open_num:
                curr += ")"
                backtrack(curr, open_num, close_num + 1)
                curr = curr[:-1]

        ans = []
        backtrack("", 0, 0)
        return ans

if __name__ == "__main__":
    runner = Solution()
    n = 3
    ans = runner.generateParenthesis(n)
    print(ans)