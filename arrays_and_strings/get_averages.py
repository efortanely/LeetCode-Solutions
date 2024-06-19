from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        print(len(nums))
        
        if k == 0:
            return nums
        elif 2*k >= len(nums):
            return [-1] * len(nums)
        else:
            ans = [-1] * k
            prefix_sum = [nums[0]]

            for i in range(1, len(nums)):
                prefix_sum += [nums[i] + prefix_sum[-1]]

            for i in range(k, len(nums) - k):
                ans += [(prefix_sum[i+k] - prefix_sum[i-k] + nums[i-k]) // (2 * k + 1)]

            ans += [-1] * k
            return ans

        
def main():
    runner = Solution()

    nums = [1,11,17,21,29]
    k = 4
    ans = runner.getAverages(nums, k)

if __name__ == "__main__":
    main()