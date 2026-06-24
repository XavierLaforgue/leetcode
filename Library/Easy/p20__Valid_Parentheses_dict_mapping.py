class Solution:
    def isValid(self, s: str) -> bool:
        lst = []
        close_open_map = {')': '(', ']': '[', '}': '{'}
        for parenthesis in s:
            if parenthesis in close_open_map and not lst:
                return False
            if parenthesis in close_open_map.values() \
                    or lst[-1] != close_open_map[parenthesis]:
                lst.append(parenthesis)
            elif lst[-1] == close_open_map[parenthesis]:
                lst.pop()
        lst_is_empty = not bool(lst)
        return lst_is_empty
