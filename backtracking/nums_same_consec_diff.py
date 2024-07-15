from typing import List

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def backtrack(curr, i):
            if i == n:
                ans.append(int("".join([str(num) for num in curr])))
                return
            
            for j in range(0 if i > 0 else 1, 10):
                if i == 0:
                    curr.append(j)
                    backtrack(curr, i+1)
                    curr.pop()
                elif abs(curr[-1] - j) == k:
                    curr.append(j)
                    backtrack(curr, i+1)
                    curr.pop()
        
        ans = []
        backtrack([], 0)
        return ans

def main():
    runner = Solution()
    n = 3
    k = 7
    ans = runner.numsSameConsecDiff(n, k)
    print(ans)

if __name__ == "__main__":
    main()