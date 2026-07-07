class Solution:
    def sumAndMultiply(self, n: int) -> int:
        n_as_str = str(n)
        digits_str = ""
        sum = 0
        for char in n_as_str:
            if char != '0':
                digits_str += char
                sum += int(char)
        x = int(digits_str) if digits_str != '' else 0
        return x * sum
