from typing import List
from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mappings = defaultdict(list)
        for i in range(len(nums)):
            mappings[nums[i]].append(i)

        for i in range(len(nums)):
            val = nums[i]
            if target - val in mappings:
                if target - val == val:
                    if len(mappings[val]) >= 2:
                        return mappings[val]
                else:
                    return [i, *mappings[target-val]]
            
        return [-1]

if __name__ == "__main__":
    runner = Solution()
    nums = [3,3]
    target = 6
    ans = runner.twoSum(nums, target)
    print(ans)