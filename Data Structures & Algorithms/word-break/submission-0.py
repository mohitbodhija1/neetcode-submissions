class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Convert to set for O(1) lookup
        word_set = set(wordDict)
        
        # dp[i] = True means s[0:i] can be segmented into dictionary words
        dp = [False] * (len(s) + 1)
        
        # Base case: empty string is always valid
        dp[0] = True
        
        # Fill dp array from left to right
        for i in range(1, len(s) + 1):
            for j in range(i):
                # If s[0:j] was breakable AND s[j:i] is a valid word
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  # No need to check further j values
        
        return dp[len(s)]