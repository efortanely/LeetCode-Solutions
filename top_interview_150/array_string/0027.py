from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ans = 0
        ptr = len(nums) - 1

        for i in range(len(nums)):
            if i > ptr:
                break

            if nums[i] != val:
                ans += 1
            else:
                while ptr > i and nums[ptr] == val:
                    ptr -= 1

                if ptr > i:
                    nums[i], nums[ptr] = nums[ptr], nums[i]
                    ptr -= 1
                    ans += 1

        return ans

if __name__ == "__main__":
    runner = Solution()
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    result = runner.removeElement(nums, val)
    print(result)
    print(nums[:result])