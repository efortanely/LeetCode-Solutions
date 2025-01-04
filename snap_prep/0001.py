class Solution(object):
    #O(n) space, O(n) complexity
    def twoSum(self, nums, target):
        num_set = {}
        for i in range(len(nums)):
            n1 = nums[i]
            n2 = target - n1
            print(n1, n2)
            if n2 in num_set:
                j = num_set[n2]
                return [i, j]
            num_set[n1] = i
        return None
