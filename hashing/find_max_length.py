from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        map = {0: -1}
        running_val = 0
        max_length = 0

        for i in range(len(nums)):
            running_val += 1 if nums[i] == 1 else -1
            if running_val in map:
                max_length = max(max_length, i - map[running_val])
            else:
                map[running_val] = i
        
        return max_length

def main():
    runner = Solution()

    nums = [0,1]
    ans = runner.findMaxLength(nums)
    print(ans)

if __name__ == "__main__":
    main()