from typing import List

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix = [nums[0]]
        ans = []

        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])

        n = len(prefix)

        for query in queries:
            left = 0
            right = n

            while left < right:
                mid = (left + right) // 2
                if prefix[mid] > query:
                    right = mid
                else:
                    left = mid + 1

            ans.append(left)

        return ans

def main():
    runner = Solution()

    nums = [4,5,2,1]
    queries = [3,10,21]
    ans = runner.answerQueries(nums, queries)
    print(ans)

if __name__ == "__main__":
    main()