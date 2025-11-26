from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        two_sum_map = {value: index for index, value in enumerate(nums)}

        for i in range(len(nums)):
            num = nums[i]
            num_pair = target - num
            if num_pair in two_sum_map and two_sum_map[num_pair] != i:
                return [i, two_sum_map[num_pair]]

if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    ans = Solution().twoSum(nums, target)
    print(ans)