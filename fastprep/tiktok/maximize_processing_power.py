from typing import List
from collections import Counter
from functools import cache

class Solution:
    def maximizeProcessingPower(self, processingPower: List[int]) -> int:
        @cache
        def dp(i):
            if i >= n:
                return 0
            
            skip = dp(i+1)

            take = analyzers[i] * powers[analyzers[i]]
            next_index = i + 1
            
            if next_index < n and analyzers[next_index] == analyzers[i] - 1:
                next_index += 1
                
            take += dp(next_index)

            return max(skip, take)
        
        if not processingPower:
            return 0
        
        powers = Counter(processingPower)
        analyzers = sorted(powers.keys(), reverse=True)
        n = len(analyzers)
        ans = dp(0)
        return ans

if __name__ == "__main__":
    runner = Solution()
    inputs = [[1, 3, 9, 2, 3], [3, 3, 5, 5, 2, 2, 5], [8, 5, 1, 5]]
    answers = [16, 21, 19]
    for x, y in zip(inputs, answers):
        output = runner.maximizeProcessingPower(x)
        print(f"{x} {output}")
        assert(output == y)