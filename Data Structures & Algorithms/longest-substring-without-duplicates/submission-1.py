class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        n = len(s)
        window = set()
        max_l = 0

        while j < n:
            # Step 1: SHRINK — if s[j] is a duplicate, shrink from the left
            while s[j] in window:
                window.remove(s[i])
                i += 1
            
            # Step 2: EXPAND — now it's safe to add s[j]
            window.add(s[j])

            # Step 3: RECORD — window is guaranteed valid here
            max_l = max(max_l, j - i + 1)

            # Step 4: MOVE j
            j += 1

        return max_l

sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))  # Output: 3
print(sol.lengthOfLongestSubstring("bbbbb"))     # Output: 1
print(sol.lengthOfLongestSubstring("pwwkew"))    # Output: 3
print(sol.lengthOfLongestSubstring("abcd"))      # Output: 4