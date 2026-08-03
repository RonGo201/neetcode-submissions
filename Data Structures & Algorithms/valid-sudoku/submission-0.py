class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cubes_set = [set() for _ in range(9)]
        for i in range(9):
            row_set = set() 
            col_set = set()
            for j in range(9):
                if ((board[i][j] != "." and board[i][j] in row_set) or 
                (board[j][i] != "." and board[j][i] in col_set) or 
                (board[i][j] != "." and board[i][j] in cubes_set[(i // 3) * 3 + (j // 3)])):
                    return False
                else:
                    row_set.add(board[i][j])
                    col_set.add(board[j][i])
                    cubes_set[(i // 3) * 3 + (j // 3)].add(board[i][j])

        return True
