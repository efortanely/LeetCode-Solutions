from typing import List
from heapq import *

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-num for num in nums]
        heapify(max_heap)
        
        ans = 0
        for _ in range(k):
            ans = heappop(max_heap)

        return -ans

def main():
    runner = Solution()
    nums = [3,2,1,5,6,4]
    k = 2
    ans = runner.findKthLargest(nums, k)
    print(ans)

if __name__ == "__main__":
    main()