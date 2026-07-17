class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        alternating = n & 1 != (n >> 1) & 1
        while alternating:
            n >>= 1
            alternating = n & 1 != (n >> 1) & 1
        return n == 0
    