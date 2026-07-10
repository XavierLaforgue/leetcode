class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if len(s) == 0:
            return 0
        count_prev = 0
        count_curr = 1
        count_subs = 0
        for idx in range(1, len(s)):
            if s[idx] == s[idx-1]:
                count_curr += 1
                if count_prev >= count_curr:
                    count_subs += 1
            else:
                count_subs += 1
                count_prev = count_curr
                count_curr = 1
        return count_subs


if __name__ == "__main__":
    print(Solution().countBinarySubstrings("10101"))
