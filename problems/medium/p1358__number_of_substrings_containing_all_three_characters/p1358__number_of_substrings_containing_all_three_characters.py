class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        if 'a' not in s or 'b' not in s or 'c' not in s:
            return 0
        cursors = [s.index('a'), s.index('b'), s.index('c')]
        cursors.sort()
        length = len(s)
        count = 0
        while True:
            count += (cursors[1] - cursors[0])\
                * (length - cursors[-1])
            first_char = s[cursors.pop(0)]
            if first_char in s[cursors[0]:]:
                new_cursor = s.index(first_char, cursors[0])
            else:
                return count
            if new_cursor < cursors[1]:
                cursors.insert(1, new_cursor)
            else:
                cursors.append(new_cursor)
