class Solution:
    def reverseBits(self, n: int) -> int:
        n_bin: str = bin(n)[2:]
        n_bin_base32: str = '0' * (32 - len(n_bin)) + n_bin
        n_bin_base32_inverted = n_bin_base32[::-1]
        return int(n_bin_base32_inverted, base=2)
