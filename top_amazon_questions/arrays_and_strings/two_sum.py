from typing import List
from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        nums_map = defaultdict(list)

        for i in range(len(nums)):
            nums_map[nums[i]].append(i)

        for i in range(len(nums)):
            num = nums[i]
            num_2 = target - num
            if num_2 in nums_map:
                if num != num_2:
                    ans.append(nums_map[num][0])
                    ans.append(nums_map[num_2][0])
                    break
                elif len(nums_map[num]) == 2:
                    ans = nums_map[num]
                    break
            
        return ans

def main():
    runner = Solution()
    nums = [3,3]
    target = 6
    ans = runner.twoSum(nums, target)
    print(ans)

if __name__ == "__main__":
    main()