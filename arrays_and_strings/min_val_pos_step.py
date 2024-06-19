from typing import List

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        running_sum = nums[0]
        lowest_val = nums[0]
        
        for n in nums[1:]:
            running_sum += n
            if running_sum < lowest_val:
                lowest_val = running_sum
        
        if lowest_val >= 0:
            return 1
        else:
            return abs(lowest_val) + 1
        
def main():
    runner = Solution()

    nums = [-3,2,-3,4,2]
    runner.minStartValue(nums)

if __name__ == "__main__":
    main()