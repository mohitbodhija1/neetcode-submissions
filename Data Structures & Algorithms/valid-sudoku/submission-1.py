from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # 9 sets for rows, cols, and 3x3 boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]

                # Skip empty cells
                if num == '.':
                    continue

                # Check ROW
                if num in rows[i]:
                    return False
                rows[i].add(num)

                # Check COL
                if num in cols[j]:
                    return False
                cols[j].add(num)

                # Check BOX
                if num in boxes[i//3][j//3]:
                    return False
                boxes[i//3][j//3].add(num)

        return True