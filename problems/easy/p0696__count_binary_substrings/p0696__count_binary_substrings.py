class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if len(s) == 0:
            return 0
        prev_char = s[0]
        count_prev, count_curr, count_subs = 0, 0, 0
        for char in s:
            if char == prev_char:
                count_curr += 1
            else:
                count_subs += min(count_prev, count_curr)  # at each bit swap
                # count outwardly how many complementing bits there were
                # around the previous bitswap and add that to the substring
                # count
                count_prev, count_curr = count_curr, 1
                prev_char = char
        count_subs += min(count_prev, count_curr)  # add the count around the
        # last bit swap
        return count_subs


if __name__ == "__main__":
    print(Solution().countBinarySubstrings("10101"))
