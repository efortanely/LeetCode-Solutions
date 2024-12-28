from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        ptr1 = m - 1
        ptr2 = n - 1
        curr = m + n -1

        while ptr1 >= 0 and ptr2 >= 0:
            if nums1[ptr1] > nums2[ptr2]:
                nums1[curr] = nums1[ptr1]
                ptr1 -= 1
            else:
                nums1[curr] = nums2[ptr2]
                ptr2 -= 1
            curr -= 1

        while ptr2 >= 0:
            nums1[curr] = nums2[ptr2]
            ptr2 -= 1
            curr -= 1

if __name__ == "__main__":
    runner = Solution()
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    runner.merge(nums1, m, nums2, n)
    print(nums1)