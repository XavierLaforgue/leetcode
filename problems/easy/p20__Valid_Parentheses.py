class Solution:
    def isValid(self, s: str) -> bool:
        lst = []
        opening = ('(', '[', '{')
        closing = (')', ']', '}')
        for parenthesis in s:
            if parenthesis in closing and not lst:
                return False
            if parenthesis in opening \
                    or lst[-1] != opening[closing.index(parenthesis)]:
                lst.append(parenthesis)
            elif lst[-1] == opening[closing.index(parenthesis)]:
                lst.pop()
        lst_is_empty = not bool(lst)
        return lst_is_empty
