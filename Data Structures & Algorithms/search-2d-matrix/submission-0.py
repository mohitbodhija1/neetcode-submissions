class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        # Step 1: Binary search for the correct row
        top, bot = 0, rows - 1
        while top <= bot:
            mid_r = (top + bot) // 2
            if matrix[mid_r][0] <= target <= matrix[mid_r][cols - 1]:
                break          # target is in this row
            elif target > matrix[mid_r][cols - 1]:
                top = mid_r + 1
            else:
                bot = mid_r - 1
        else:
            return False       # no row could contain target

        # Step 2: Binary search within that row
        lo, hi = 0, cols - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if matrix[mid_r][mid] == target:
                return True
            elif matrix[mid_r][mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1   # ← your bug was `e -= 1` here

        return False