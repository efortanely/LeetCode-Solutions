from typing import List

class Solution:
    def countElements(self, arr: List[int]) -> int:
        arr_set = set(arr)
        ans = 0

        for num in arr:
            if num + 1 in arr_set:
                ans += 1

        return ans
        
def main():
    runner = Solution()

    arr = [1,1,3,3,5,5,7,7]
    ans = runner.countElements(arr)
    print(ans)

if __name__ == "__main__":
    main()