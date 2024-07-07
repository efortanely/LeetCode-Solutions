from typing import List
from heapq import *

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        min_heap = sticks
        heapify(min_heap)
        cost = 0

        while len(min_heap) > 1:
            stick_1 = heappop(min_heap)
            stick_2 = heappop(min_heap)
            new_stick = stick_1 + stick_2

            cost += new_stick
            heappush(min_heap, new_stick)

        return cost

def main():
    runner = Solution()

    sticks = [1,8,3,5]
    ans = runner.connectSticks(sticks)
    print(ans)

if __name__ == "__main__":
    main()