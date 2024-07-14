from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(largest_sum) -> bool:
            num_splits = 0
            curr_sum = 0

            for num in nums:
                if curr_sum + num > largest_sum:
                    num_splits += 1
                    curr_sum = num
                else:
                    curr_sum += num
            
            return num_splits + 1 <= k
        
        left = max(nums)
        right = sum(nums)

        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left

def main():
    runner = Solution()
    nums = [1,4,4]
    k = 3
    ans = runner.splitArray(nums, k)
    print(ans)

if __name__ == "__main__":
    main()