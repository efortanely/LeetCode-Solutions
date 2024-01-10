from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        sorted_neg = []

        for n in nums:
            if n < 0:
                sorted_neg += [n ** 2]
            elif n >= 0 and len(sorted_neg) > 0:
                sq = n ** 2
                smallest_neg = sorted_neg[-1]

                while sq > smallest_neg:
                    ans += [smallest_neg]
                    sorted_neg = sorted_neg[:-1]

                    if sorted_neg:
                        smallest_neg = sorted_neg[-1]
                    else:
                        smallest_neg = float('inf')

                ans += [sq]
            else:
                ans += [n ** 2]

        if sorted_neg:
            ans += sorted_neg[::-1]

        return ans
    
def main():
    runner = Solution()

    nums = [-4,-1,0,3,10]
    ans = runner.sortedSquares(nums)
    print(ans)

if __name__ == "__main__":
    main()