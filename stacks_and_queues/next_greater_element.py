from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        decreasing = []
        # for each value in nums2, what is the index of the next greater value
        next_greater_val_idx = [-1] * len(nums2)
        map = {}

        for i in range(len(nums2)):
            while decreasing and nums2[decreasing[-1]] < nums2[i]:
                j = decreasing.pop()
                
                # if a number gets popped it was smaller than nums2[i]
                # i is the index of the next greater value
                next_greater_val_idx[j] = i
            
            decreasing.append(i)
            map[nums2[i]] = i
        
        ans = []

        for i in range(len(nums1)):
            nums1_val = nums1[i]
            nums2_idx = map[nums1_val]
            idx = next_greater_val_idx[nums2_idx]
            next_greater = -1 if idx == -1 else nums2[idx]
            ans.append(next_greater)

        return ans

def main():
    runner = Solution()

    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    ans = runner.nextGreaterElement(nums1, nums2)
    print(ans)

if __name__ == "__main__":
    main()