class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_len = len(a)
        b_len = len(b)
        max_len = max(a_len, b_len)
        a = (b_len-a_len) * '0' + a
        b = (a_len-b_len) * '0' + b
        carried = 0
        c = ""
        for i in range(max_len):
            i += 1
            int_sum = int(a[-i]) + int(b[-i]) + carried
            carried = int_sum // 2
            c = str(int_sum) + c if int_sum < 2 else str(int_sum % 2) + c
        if carried == 1:
            return '1' + c
        return c
