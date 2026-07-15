class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd: int = sum(2 * m + 1 for m in range(n))
        sumEven: int = sum(2 * (m + 1) for m in range(n))
        # Euclidian algorithm:
        greater = sumEven
        lesser = sumOdd
        while lesser != 0:
            greater, lesser = lesser, greater % lesser
        return greater
