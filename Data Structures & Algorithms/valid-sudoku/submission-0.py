class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = [list(col) for col in zip(*board)]
        size = 3
        rows = len(board)
        cols = len(board[0])
        
        for row in board:
            nums = [r for r in row if r!='.']
            if len(nums) != len(set(nums)):
                return False
            
        for col in columns:
            print(col)
            nums = [c for c in col if c!='.']
            if len(nums) != len(set(nums)):
                return False
        
        for i in range(0, rows - size + 1, size):
            for j in range(0, cols - size + 1, size):
                window = [
                    board[i + r][j:j + size]
                    for r in range(size)
                ]

                flat = [x for row in window for x in row if x != '.']

                if len(flat) != len(set(flat)):
                    return False

        return True