class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        all_nums = set(nums1).union(set(nums2))
        ans = [list(all_nums - set(nums2)), list(all_nums - set(nums1))]

        return ans