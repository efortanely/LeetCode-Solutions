from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1
        
        pivot_idx = left
        left, right = 0, len(nums) - 1

        if nums[pivot_idx] <= target <= nums[right]:
            left = pivot_idx
        else:
            right = pivot_idx - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1

if __name__ == "__main__":
    runner = Solution()
    nums = [[1,3,5], [3,1], [4,5,6,7,0,1,2], [4,5,6,7,0,1,2], [1], [1,3]]
    target = [5, 3, 0, 3, 0, 3]
    ans = [2, 0, 4, -1, -1, 1]

    for n, t, a in zip(nums, target, ans):
        result = runner.search(n, t)
        print(f"nums={n} target={t} output={result} ans={a}")
        assert(result == a)