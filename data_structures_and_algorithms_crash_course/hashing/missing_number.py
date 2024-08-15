from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans_set = set(range(0, len(nums) + 1))

        for n in nums:
            ans_set.remove(n)

        return ans_set.pop()
        
def main():
    runner = Solution()

    nums = [9,6,4,2,3,5,7,0,1]
    ans = runner.missingNumber(nums)
    print(ans)

if __name__ == "__main__":
    main()