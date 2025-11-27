from typing import List
from collections import Counter

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    ans.add((nums[i], nums[left], nums[right]))
                    left += 1
                elif sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1

        return [[x, y, z] for x, y, z in ans] 

if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    ans = Solution().threeSum(nums)
    print(ans)