class Solution:
    def swap(self, nums, x, y):
        tmp = nums[x]
        nums[x] = nums[y]
        nums[y] = tmp
        
    def reverse(self, nums, start, end):
        while start < end:
            self.swap(nums, start, end)
            start += 1
            end -= 1
    
    def nextPermutation(self, nums: List[int]) -> None:
        k = None
        for i in range(len(nums) - 2, -2, -1):
            k = i
            if nums[i] < nums[i+1]:
                break
        if k < 0:
            nums.reverse()
        else:
            l = None
            for i in range(len(nums) - 1, k, -1):
                l = i
                if nums[i] > nums[k]:
                    break
            
            self.swap(nums, k, l)
            self.reverse(nums, k+1, len(nums)-1)
