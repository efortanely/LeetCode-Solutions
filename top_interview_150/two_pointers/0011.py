from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = float("-inf")

        while left < right:
            area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

if __name__ == "__main__":
    runner = Solution()
    height = [1,1]
    ans = runner.maxArea(height)
    print(ans)