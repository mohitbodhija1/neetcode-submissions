class Solution:
    def getSum(self,a: int, b: int) -> int:
        # 32-bit mask to handle Python's arbitrary precision integers
        MASK = 0xFFFFFFFF
        MAX  = 0x7FFFFFFF  # Maximum positive value for 32-bit signed integer
        
        while b != 0:
            # Carry: positions where both bits are 1, shifted left
            carry = (a & b) << 1
            
            # Sum without carry
            a = (a ^ b) & MASK
            
            # Carry becomes the new b
            b = carry & MASK
        
        # If a is within positive 32-bit range, return as is
        # Otherwise convert from two's complement to Python negative integer
        return a if a <= MAX else ~(a ^ MASK)