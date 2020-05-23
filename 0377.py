class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        M = [0 for i in range(target + 1)]
        M[0] = 1

        for i in range(1, target + 1):
            for n in nums:
                if n <= i:
                    M[i] += M[i-n]

        return M[-1]
