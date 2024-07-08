from typing import List
from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        counter = Counter(arr)
        sorted_counter = sorted([(k,v) for k, v in counter.items()], key=lambda x: -x[1])
        
        for i in range(len(arr)):
            _, occur = sorted_counter[i]
            n -= occur
            if n <= len(arr) // 2:
                return i + 1

        return -1

def main():
    runner = Solution()

    arr = [1,9]
    ans = runner.minSetSize(arr)
    print(ans)

if __name__ == "__main__":
    main()
