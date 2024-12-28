from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        col_sets = [set() for _ in range(n)]
        row_sets = [set() for _ in range(n)]

        for i in range(n):
            for j in range(n):
                val = board[i][j]
                if val == ".":
                    continue

                if val in col_sets[j]:
                    return False
                else:
                    col_sets[j].add(val)

                if val in row_sets[i]:
                    return False
                else:
                    row_sets[i].add(val)

        for i in range(0, n, 3):
            for j in range(0, n, 3):
                seen = set()
                for k in range(3):
                    for l in range(3):
                        val = board[i+k][j+l]
                        if val == ".":
                            continue

                        if val in seen:
                            return False
                        else:
                            seen.add(val)

        return True

if __name__ == "__main__":
    runner = Solution()
    board = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    ans = runner.isValidSudoku(board)
    print(ans)