from typing import List

class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        max_weight = 5000
        ans = 0

        for i in range(len(weight)):
            if weight[i] <= max_weight:
                max_weight -= weight[i]
                ans += 1
            else:
                break

        return ans
    
def main():
    runner = Solution()

    weight = [900,950,800,1000,700,800]
    ans = runner.maxNumberOfApples(weight)
    print(ans)

if __name__ == "__main__":
    main()