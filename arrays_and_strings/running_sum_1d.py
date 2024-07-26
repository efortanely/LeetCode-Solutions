from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]

        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])

        return prefix

def main():
    runner = Solution()

    nums = [3,1,2,10,1]
    ans = [3,4,6,16,17]
    testcase = runner.runningSum(nums)
    print(testcase)

if __name__ == "__main__":
    main()