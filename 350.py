class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        dic = dict()

        for n in nums1:
            dic[n] = dic[n] + 1 if n in dic else 1
            
        for n in nums2:
            if n in dic:
                ans.append(n)
                dic[n] -= 1
                if dic[n] is 0:
                    del dic[n]
            
        return ans
