class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        visited = [[False for j in range(len(matrix[0]))] for i in range(len(matrix))]
        #         R      D       L      U
        move = ((0,1), (1,0), (0,-1), (-1,0))
        move_idx = 0
        ans = []
        i, j = 0, 0
        
        while not visited[i][j]:
            ans.append(matrix[i][j])
            visited[i][j] = True
            #update amount to increase i, j by from our defined movement tuples
            move_i, move_j = move[move_idx][0], move[move_idx][1]
            move_out_of_bounds = i+move_i < 0 or i+move_i >= len(matrix) or \
                                j+move_j < 0 or j+move_j >= len(matrix[0])
            
            #if this move is outside the array or is a visited index, 
            #update the movement direction and amount to increase i, j by
            if move_out_of_bounds or visited[i+move_i][j+move_j]:
                move_idx = (move_idx + 1) % 4
                move_i, move_j = move[move_idx][0], move[move_idx][1]
            
            #if the move is inside the array, increase i, j
            if i+move_i >= 0 and i+move_i < len(matrix) and j+move_j >= 0 and \
                j+move_j < len(matrix[0]):
                i, j = i + move_i, j + move_j
            
        return ans
