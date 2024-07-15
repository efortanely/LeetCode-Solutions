from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(curr, left_count, right_count):
            if len(curr) == n * 2:
                ans.append(curr[:])
                return
            
            if left_count < n:
                curr += "("
                backtrack(curr, left_count+1, right_count)
                curr = curr[:-1]
            if right_count < left_count:
                curr += ")"
                backtrack(curr, left_count, right_count+1)
                curr = curr[:-1]

        ans = []
        backtrack("", 0, 0)
        return ans

def main():
    runner = Solution()
    n = 3
    ans = runner.generateParenthesis(n)
    print(ans)

if __name__ == "__main__":
    main()