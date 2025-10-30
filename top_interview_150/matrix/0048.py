from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for row in range(n // 2 + n % 2):
            for col in range(n // 2):
                tmp = matrix[n - 1 - col][row]
                matrix[n - 1 - col][row] = matrix[n - 1 - row][n - col - 1]
                matrix[n - 1 - row][n - col - 1] = matrix[col][n - 1 - row]
                matrix[col][n - 1 - row] = matrix[row][col]
                matrix[row][col] = tmp
                
if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Solution().rotate(matrix)
    assert matrix == [[7,4,1],[8,5,2],[9,6,3]]