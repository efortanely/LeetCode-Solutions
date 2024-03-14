from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = flip = ans = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                flip += 1
            while flip > k:
                if nums[left] == 0:
                    flip -= 1
                left += 1
            ans = max(ans, right - left + 1)
        
        return ans
        
    
def main():
    runner = Solution()

    nums = [1,1,1,0,0,0,1,1,1,1,0]
    k = 2
    testcase = runner.longestOnes(nums, k)
    print(testcase)

if __name__ == "__main__":
    main()