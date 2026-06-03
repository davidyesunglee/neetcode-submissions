class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])

        for row in board:
            seen = set()
            
            for val in row:
                if val == '.':
                    continue
                
                if val in seen:
                    return False
                
                seen.add(val)

        for col in range(9):
            seen = set()
            
            for row in range(9):
                val = board[row][col]

                if val == '.':
                    continue
                
                if val in seen:
                    return False
                
                seen.add(val)

        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                seen = set()

                for r in range(row, row + 3):
                    for c in range(col, col + 3):
                        val = board[r][c]
                        if val == '.':
                            continue
                        if val in seen:
                            return False
                        seen.add(val)

        return True
