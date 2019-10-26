class Solution(object):
    #O(n) space, O(n) complexity
    def twoSum(self, nums, target):
        num_set = {}
        for i in range(len(nums)):
            n1 = nums[i]
            n2 = target - n1
            num_set[n1] = i
            if n2 in num_set:
                j = num_set[n2]
                return [i, j]
        return None
