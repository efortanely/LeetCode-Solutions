from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(curr, used_nums):
            if len(curr) == k and sum(curr) == n:
                ans.append(curr[:])
                return
            
            for i in range(1 if not curr else curr[-1] + 1, 10):
                if i not in used_nums and sum(curr) + i <= n:
                    curr.append(i)
                    used_nums.add(i)
                    backtrack(curr, used_nums)
                    curr.pop()
                    used_nums.remove(i)

        ans = []
        backtrack([], set())
        return ans

def main():
    runner = Solution()
    k = 3
    n = 9
    ans = runner.combinationSum3(k, n)
    print(ans)

if __name__ == "__main__":
    main()