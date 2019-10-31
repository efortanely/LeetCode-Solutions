class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] is word[0]:
                    if self.exist_square(i, j, board, word[1:]):
                        return True
        return False
        
        return exists
                
    def exist_square(self, i: int, j: int, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        
        temp = board[i][j]
        board[i][j] = ''
        
        for new_i, new_j in {(i-1,j), (i,j-1), (i,j+1), (i+1,j)}:
            nbr = ''
            if new_i >= 0 and new_j >= 0 and new_i < len(board) and new_j < len(board[0]):
                nbr = board[new_i][new_j]
            if nbr is word[0]:
                if self.exist_square(new_i, new_j, board, word[1:]):
                    return True
        
        board[i][j] = temp
        
        return False
