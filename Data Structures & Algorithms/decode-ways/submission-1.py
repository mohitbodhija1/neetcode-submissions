class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        # Edge case: string starting with '0' has no valid decoding
        if s[0] == '0':
            return 0

        # dp[i] = number of ways to decode s[0..i-1]
        # dp has n+1 elements so dp[n] is our answer
        dp = [0] * (n + 1)

        dp[0] = 1   # base: empty string has one way to decode
        dp[1] = 1   # base: s[0] is guaranteed non-zero from check above

        for i in range(2, n + 1):

            one_digit = int(s[i-1])       # s[i-1]      e.g. "6"
            two_digit = int(s[i-2:i])     # s[i-2..i-1] e.g. "26"

            # Take 1 step: current char alone is valid if it's not '0'
            if one_digit != 0:
                dp[i] += dp[i-1]

            # Take 2 steps: previous two chars valid if between 10 and 26
            # NOTE: must be >= 10, so leading zero like "06" is invalid
            if 10 <= two_digit <= 26:
                dp[i] += dp[i-2]

        return dp[n]


# ── Tests ──────────────────────────────────────────────
print(Solution().numDecodings("226"))     # 3
print(Solution().numDecodings("12"))      # 2  → "AB" or "L"
print(Solution().numDecodings("06"))      # 0  → leading zero
print(Solution().numDecodings("10"))      # 1  → "J" only (1,0 invalid)
print(Solution().numDecodings("110"))     # 1  → "1","10" = AJ only