from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix[0])

        for i in range(n//2 + n%2):
            for j in range(n//2):
                temp = matrix[n-1-i][j]
                matrix[n-1-i][j] = matrix[n-1-j][n-1-i]
                matrix[n-1-j][n-1-i] = matrix[i][n-1-j]
                matrix[i][n-1-j] = matrix[j][i]
                matrix[j][i] = temp

def main():
    runner = Solution()
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    runner.rotate(matrix)
    print(matrix)

if __name__ == "__main__":
    main()