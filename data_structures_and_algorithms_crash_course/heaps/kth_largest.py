from typing import List
from heapq import *

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums
        heapify(self.min_heap)
        
        while len(self.min_heap) > k:
            heappop(self.min_heap)

    def add(self, val: int) -> int:
        heappush(self.min_heap, val)

        if len(self.min_heap) > self.k:
            heappop(self.min_heap)

        return self.min_heap[0]
    
def main():
    k = 3
    nums = [4, 5, 8, 2]

    kth_largest = KthLargest(k, nums)
    print(kth_largest.add(3))
    print(kth_largest.add(5))
    print(kth_largest.add(10))
    print(kth_largest.add(9))
    print(kth_largest.add(4))

if __name__ == "__main__":
    main()