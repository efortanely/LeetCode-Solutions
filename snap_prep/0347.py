class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        num_lists = []
        num_list = []
        
        for num in nums:
            if not num_list or num == num_list[0]:
                num_list.append(num)
            else:
                num_lists.append(num_list)
                num_list = [num]
        
        if num_list:
            num_lists.append(num_list)
        
        num_lists.sort(key = len)
        ans = []
        for i in range(1, k+1):
            ans.append(num_lists[-i][0])
        return ans
