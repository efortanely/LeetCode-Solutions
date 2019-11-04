class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.pathHelper(0, 0, m, n)
    
    def pathHelper(self, i: int, j: int, m: int, n: int) -> int:
            if i == m-1 and j == n-1:
                return 1
            else:
                count = 0
                if i+1 < m:
                    count += self.pathHelper(i+1, j, m, n)
                if j+1 < n:
                    count += self.pathHelper(i, j+1, m, n)
                return count
