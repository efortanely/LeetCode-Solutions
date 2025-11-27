from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row, curr, used_cols, used_main_diags, used_anti_diags):
            if row == n:
                ans.append(curr[:])
                return
            
            for col in range(n):
                if col in used_cols or (row - col) in used_main_diags or (row + col) in used_anti_diags:
                    continue 
                
                curr[row] = ("." * col) + "Q" + ("." * (n - col - 1))
                used_cols.add(col)
                used_main_diags.add(row - col)
                used_anti_diags.add(row + col)

                backtrack(row + 1, curr, used_cols, used_main_diags, used_anti_diags)
                
                used_cols.remove(col)
                used_main_diags.remove(row - col)
                used_anti_diags.remove(row + col)
                curr[row] = "." * n
    
        ans = []
        backtrack(0, [("." * n) for i in range(n)], set(), set(), set())
        return ans

if __name__ == "__main__":
    n = 4
    ans = Solution().solveNQueens(n)
    print(ans)