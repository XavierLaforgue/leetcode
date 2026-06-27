class Solution:
    def isValid(self, s: str) -> bool:
        lst = []
        closing = {')', ']', '}'}
        opening = {'(', '[', '{'}
        close_to_open = {')': '(', ']': '[', '}': '{'}
        for par in s:
            if par in closing and not lst:
                return False
            if par in opening \
                    or lst[-1] != close_to_open[par]:
                lst.append(par)
            elif lst[-1] == close_to_open[par]:
                lst.pop()
        return not bool(lst)
