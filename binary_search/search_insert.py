from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1

        return left
    
def main():
    runner = Solution()

    nums = [1,3,5,6]
    target = 5
    ans = runner.searchInsert(nums, target)
    print(ans)

if __name__ == "__main__":
    main()