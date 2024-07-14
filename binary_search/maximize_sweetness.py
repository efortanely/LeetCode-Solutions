from typing import List

class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        def check(curr_sweetness) -> bool:
            num_bars = 0
            curr_bar_sweetness = 0
            
            for bar in sweetness:
                curr_bar_sweetness += bar

                if curr_bar_sweetness >= curr_sweetness:
                    num_bars += 1
                    curr_bar_sweetness = 0
            
            return num_bars >= k + 1
        
        left = min(sweetness)
        right = sum(sweetness)

        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        
        return right

def main():
    runner = Solution()
    sweetness = [1,2,3,4,5,6,7,8,9]
    k = 5

    ans = runner.maximizeSweetness(sweetness, k)
    print(ans)

if __name__ == "__main__":
    main()