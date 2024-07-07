from typing import List
from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        numbered_board = [[0 for _ in range(n)] for _ in range(n)]
        num_to_idx = {}

        count = 1
        left_to_right = True

        for row in range(n-1, -1, -1):
            if left_to_right:
                for col in range(n):
                    numbered_board[row][col] = count
                    num_to_idx[count] = (row, col)
                    count += 1
            else:
                for col in range(n-1, -1, -1):
                    numbered_board[row][col] = count
                    num_to_idx[count] = (row, col)
                    count += 1

            left_to_right = not left_to_right
                
        queue = deque([(1, 0)]) #board number, steps
        seen = {1}

        while queue:
            board_number, steps = queue.popleft()
            row, col = num_to_idx[board_number]
            
            if board_number == n**2:
                return steps
                        
            for next_step_num in range(board_number + 1, min(board_number + 6, n**2) + 1):
                next_row, next_col = num_to_idx[next_step_num]
                final_number = board[next_row][next_col] if board[next_row][next_col] != -1 else next_step_num

                if final_number not in seen:
                    seen.add(final_number)
                    queue.append((final_number, steps + 1))
            
        return -1
    
def main():
    runner = Solution()

    board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
    ans = runner.snakesAndLadders(board)
    print(ans)

if __name__ == "__main__":
    main()