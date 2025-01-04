class Solution:
    '''
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        nums2 = list(set(nums))
        nums.sort()
        nums2.sort()
        return not nums == nums2
    '''
    
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums2 = set()
        for n in nums:
            if n in nums2:
                return True
            nums2.add(n)
        return False
