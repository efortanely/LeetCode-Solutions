import math

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    for k in range(len(matrix)):
                        if matrix[k][j] != 0:
                            matrix[k][j] = -math.inf
                    for k in range(len(matrix[0])):
                        if matrix[i][k] != 0:
                            matrix[i][k] = -math.inf
                            
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == -math.inf:
                    matrix[i][j] = 0
