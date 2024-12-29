from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = [nums[0]]
        suffix_prod = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix_prod.append(prefix_prod[-1] * nums[i])

        for i in range(len(nums)-2, -1, -1):
            suffix_prod[i] = suffix_prod[i+1] * nums[i+1]

        ans = []
        for i in range(len(nums)):
            if i > 0:
                prod = prefix_prod[i-1] * suffix_prod[i]
            else:
                prod = suffix_prod[i]
            
            ans.append(prod)
            
        return ans

if __name__ == "__main__":
    runner = Solution()
    nums = [-1,1,0,-3,3]
    ans = runner.productExceptSelf(nums)
    print(ans)