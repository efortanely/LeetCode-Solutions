from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = 0
        ans = 0

        for i in range(k):
            curr += nums[i]
        
        ans = curr / k
        
        for i in range(k, len(nums)):
            curr -= nums[i-k]
            curr += nums[i]
            avg = curr / k
            ans = max(ans, avg)

        return ans
        
    
def main():
    runner = Solution()

    nums = [5]
    k = 1
    testcase = runner.findMaxAverage(nums, k)
    print(testcase)

if __name__ == "__main__":
    main()