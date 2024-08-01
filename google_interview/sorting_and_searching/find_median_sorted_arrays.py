from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_array = []

        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                merged_array.append(nums1[i])
                i += 1
            elif nums2[j] < nums1[i]:
                merged_array.append(nums2[j])
                j += 1

        if i < len(nums1):
            merged_array += nums1[i:]
        elif j < len(nums2):
            merged_array += nums2[j:]
        
        n = len(merged_array)
        if n % 2 == 0:
            return (merged_array[n//2] + merged_array[n//2 - 1])/2
        else:
            return merged_array[n//2]


def main():
    runner = Solution()
    nums1 = [1,2]
    nums2 = [3,4]
    ans = runner.findMedianSortedArrays(nums1, nums2)
    print(ans)

if __name__ == "__main__":
    main()