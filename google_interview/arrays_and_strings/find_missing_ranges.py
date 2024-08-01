from typing import List

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if not nums:
            return [[lower, upper]]
        
        ans = []

        if nums[0] > lower:
            ans.append([lower, nums[0] - 1])
        
        for i in range(1, len(nums)):
            curr = nums[i]
            prev = nums[i-1]

            if curr > prev + 1:
                ans.append([prev + 1, curr - 1])

        if nums[-1] < upper:
            ans.append([nums[-1] + 1, upper])

        return ans

def main():
    runner = Solution()
    nums = [-1]
    lower = -1
    upper = -1
    ans = runner.findMissingRanges(nums, lower, upper)
    print(ans)

if __name__ == "__main__":
    main()