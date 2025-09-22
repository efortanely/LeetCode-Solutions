from typing import List, Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return counter.most_common()[0][0]

if __name__ == "__main__":
    nums = [3,2,3]
    ans = Solution().majorityElement(nums)
    print(ans)
    assert ans == 3