class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        def get_sequence(num: int, get_next: bool = False):
            next_digit = int(get_next)
            first_digit = num
            max_power = 0
            while first_digit > 9:
                first_digit //= 10
                max_power += 1
            first_digit += next_digit
            jump = first_digit + max_power > 9
            max_power += int(jump)
            if jump:
                first_digit = 1
            sequence = 0
            for n in range(max_power + 1):
                sequence += (first_digit + max_power - n) * 10 ** n
            return sequence
        start = get_sequence(low)
        if start < low:
            start = get_sequence(start, True)
        seq = []
        while start <= high:
            seq.append(start)
            start = get_sequence(start, True)
        return seq
