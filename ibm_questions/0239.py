from typing import List
from heapq import *

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = [(-nums[i], i) for i in range(k)]
        heapify(max_heap)
        ans = [-max_heap[0][0]]

        for i in range(k, len(nums)):
            heappush(max_heap, (-nums[i], i))

            while max_heap[0][1] <= i - k:
                heappop(max_heap)

            ans.append(-max_heap[0][0])

        return ans

if __name__ == "__main__":
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    ans = Solution().maxSlidingWindow(nums, k)
    print(ans)
