from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        nums_set = set(nums)

        for num in nums_set:
            if num - 1 not in nums_set:
                curr = num
                length = 1

                while curr + 1 in nums_set:
                    curr += 1
                    length += 1

                ans = max(ans, length)
        
        return ans

if __name__ == "__main__":
    nums = [100,4,200,1,3,2]
    ans = Solution().longestConsecutive(nums)
    print(ans)