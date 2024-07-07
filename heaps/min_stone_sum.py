from typing import List
from heapq import *

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        max_heap = [-pile for pile in piles]
        heapify(max_heap)

        for _ in range(k):
            pile = heappop(max_heap)
            pile //= 2
            heappush(max_heap, pile)

        return abs(sum(max_heap))

def main():
    runner = Solution()

    piles = [5,4,9]
    k = 2
    ans = runner.minStoneSum(piles, k)
    print(ans)

if __name__ == "__main__":
    main()