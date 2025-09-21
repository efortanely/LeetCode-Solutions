from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def getPrev(i):
            if i < 0:
                return float("-inf")
            
            return nums[i]
        
        def getNext(i):
            if i == len(nums):
                return float("-inf")
            
            return nums[i]

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if getPrev(mid-1) < nums[mid] and nums[mid] > getNext(mid+1):
                break
            if nums[mid] > getNext(mid+1):
                right = mid - 1
            else:
                left = mid + 1
        
        return mid

if __name__ == "__main__":
    runner = Solution()
    nums = [1,2,3,1]
    ans = runner.findPeakElement(nums)
    print(ans)