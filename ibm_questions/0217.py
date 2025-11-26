from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    ans = Solution().containsDuplicate(nums)
    print(ans)