from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-x for x in nums]
        heapq.heapify(heap)
        
        for _ in range(k - 1):
            heapq.heappop(heap)

        return -heapq.heappop(heap)

if __name__ == "__main__":
    runner = Solution()
    nums = [3,2,1,5,6,4]
    k = 2
    ans = runner.findKthLargest(nums, k)
    print(ans)
    assert ans == 5