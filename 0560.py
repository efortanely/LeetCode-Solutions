class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = dict()
        sums[0] = 1
        sum_ct = 0
        ans = 0
        
        for n in nums:
            sum_ct += n
            num_seek = sum_ct - k
            
            if num_seek in sums:
                ans += sums[num_seek]
            
            sums[sum_ct] = (sums[sum_ct] if sum_ct in sums else 0) + 1
            
        return ans
