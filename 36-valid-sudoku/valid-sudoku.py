class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Use sets to track seen numbers for each row, column, and 3×3 box
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue  # skip empty cells
                
                # Compute index of the 3×3 box
                box_index = (i // 3) * 3 + (j // 3)
                
                # Check if we've already seen this number in the row, column, or box
                if (val in rows[i] or
                    val in cols[j] or
                    val in boxes[box_index]):
                    return False
                
                # Mark this number as seen
                rows[i].add(val)
                cols[j].add(val)
                boxes[box_index].add(val)
        
        return True
