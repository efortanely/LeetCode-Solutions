class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        k = len(nums)//2
        elems = dict()
        for num in nums:
            if num not in elems:
                elems[num] = 1
            else:
                elems[num] += 1
            
            if elems[num] > k:
                return num
