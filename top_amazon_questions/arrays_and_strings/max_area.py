from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        ans = (right - left) * min(height[left], height[right])

        while left < right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            
            ans = max(ans, (right - left) * min(height[left], height[right]))

        return ans

        
def main():
    runner = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    ans = runner.maxArea(height)
    print(ans)

if __name__ == "__main__":
    main()