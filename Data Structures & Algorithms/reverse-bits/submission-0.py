class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        
        for _ in range(32):
            # Step 1: Extract the rightmost bit of n
            bit = n & 1
            
            # Step 2: Make room in result and place the bit
            result = (result << 1) | bit
            
            # Step 3: Move to the next bit of n
            n >>= 1
        
        # Ensure 32-bit unsigned integer (important for Python)
        return result & 0xFFFFFFFF