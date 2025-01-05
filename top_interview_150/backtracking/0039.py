from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(curr, i):
            curr_sum = sum(curr)
            if curr_sum > target:
                return
            if curr_sum == target:
                ans.append(curr[:])
                return

            for j in range(i, len(candidates)):
                curr.append(candidates[j])
                backtrack(curr, j)
                curr.pop()

        ans = []
        backtrack([], 0)
        return ans

if __name__ == "__main__":
    runner = Solution()
    candidates = [2,3,6,7]
    target = 7
    ans = runner.combinationSum(candidates, target)
    print(ans)