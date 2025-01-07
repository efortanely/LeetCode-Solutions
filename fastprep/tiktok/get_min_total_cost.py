from typing import List
from heapq import *

class Solution:
    def getMinimumTotalCost(self, vouchersCount: int, prices: List[int]) -> int:
        max_heap = [-price for price in prices]
        heapify(max_heap)

        while vouchersCount > 0:
            price = -heappop(max_heap)
            price //= 2
            heappush(max_heap, -price)
            vouchersCount -= 1

        return -sum(max_heap)

if __name__ == "__main__":
    runner = Solution()
    voucher_input = 3
    price_input = [8, 2, 13]
    answer = 9
    output = runner.getMinimumTotalCost(voucher_input, price_input)
    print(f"{voucher_input}, {price_input} = {output}")
    assert(output == answer)