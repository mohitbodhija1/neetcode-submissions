class Solution:
   
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""

        best_start, best_end = 0, 0

        def expand(left: int, right: int) -> tuple[int, int]:
            # Expand outward while characters match
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            # When loop exits, s[left] != s[right] (or out of bounds)
            # So last valid window was [left+1, right-1]
            return left + 1, right - 1

        for i in range(n):
            # Case 1: odd-length palindrome — center is character i
            l1, r1 = expand(i, i)

            # Case 2: even-length palindrome — center is gap between i and i+1
            l2, r2 = expand(i, i + 1)

            # Update best if this expansion is longer
            if r1 - l1 > best_end - best_start:
                best_start, best_end = l1, r1

            if r2 - l2 > best_end - best_start:
                best_start, best_end = l2, r2

        return s[best_start : best_end + 1]


