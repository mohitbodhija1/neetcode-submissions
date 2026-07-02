class Solution:
    def hammingWeight(self, n: int) -> int:
            count = 0

            while n:              # keep going until n becomes 0
                count += n & 1    # check if last bit is 1
                n >>= 1           # shift right by 1 (drop last bit)

            return count