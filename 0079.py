class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if self.exist_square(i, j, board, word):
                    return True
        return False
                
    def exist_square(self, i: int, j: int, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] is not word[0]:
            return False
        
        temp = board[i][j]
        board[i][j] = ''
        
        exist = self.exist_square(i-1,j,board,word[1:]) or self.exist_square(i,j-1,board,word[1:]) or\
                self.exist_square(i,j+1,board,word[1:]) or self.exist_square(i+1,j,board,word[1:])
        
        board[i][j] = temp
        
        return exist
