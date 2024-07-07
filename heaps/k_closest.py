from typing import List
from heapq import *

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for point in points:
            x, y = point
            dist_sq = x**2 + y**2
            heappush(max_heap, (-dist_sq, x, y))

            if len(max_heap) > k:
                heappop(max_heap)

        return [[point[1], point[2]] for point in max_heap]

def main():
    runner = Solution()

    points = [[3,3],[5,-1],[-2,4]]
    k = 2
    ans = runner.kClosest(points, k)

    print(ans)

if __name__ == "__main__":
    main()