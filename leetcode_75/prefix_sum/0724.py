class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [nums[0]]

        for num in nums[1:]:
            prefix.append(prefix[-1] + num)

        for i in range(len(prefix)):
            if i == 0 and prefix[-1] - prefix[i] == 0:
                return i
            elif i > 0 and prefix[i-1] == prefix[-1] - prefix[i]:
                return i
        
        return -1