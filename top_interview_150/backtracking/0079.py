from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        last_char = word[-1]
        last_char_pos = [(i, j) for i in range(len(board)) for j in range(len(board[i])) if board[i][j] == last_char]

        for start_pos in last_char_pos:
            stack = [(start_pos, word[-1], {start_pos})]

            while stack:
                idx, word_seen, idx_seen = stack.pop()

                if word_seen == word:
                    return True

                next_char = word[-len(word_seen) - 1]
                dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

                for move in dir:
                    next_pos = (idx[0] + move[0], idx[1] + move[1])

                    if next_pos[0] < 0 or next_pos[0] >= len(board) or next_pos[1] < 0 or next_pos[1] >= len(board[0]) \
                        or next_pos in idx_seen or board[next_pos[0]][next_pos[1]] != next_char:
                        continue

                    new_visited = idx_seen | {next_pos}
                    stack.append((next_pos, next_char + word_seen, new_visited))

        return False

if __name__ == "__main__":
    board = [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]]
    word = "AAAAAAAAAAAAAAa"
    ans = Solution().exist(board, word)
    print(ans)