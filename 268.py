class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        set1 = set()
        for i in range(len(nums)+1):
            set1.add(i)
        return set1.difference(set(nums)).pop()
