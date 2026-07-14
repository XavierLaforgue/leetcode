class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_n = 0
        for _ in range(32):
            last_bit = n & 0b1
            reversed_n = (reversed_n << 1) | last_bit
            n >>= 1
        return reversed_n
