class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd: int = sum(2 * m + 1 for m in range(n))
        sumEven: int = sum(2 * (m + 1) for m in range(n))
        # Euclid algorithm:
        greater = sumOdd
        lesser = sumEven - sumOdd
        while greater != lesser:
            if greater > lesser:
                greater, lesser = lesser, greater - lesser
            else:
                greater, lesser = greater, lesser - greater
        return greater

if __name__ == "__main__":
    Solution().gcdOfOddEvenSums(3)
