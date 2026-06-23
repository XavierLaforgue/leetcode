class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        number_of_strings = len(strs)
        if number_of_strings == 1:
            return strs[0]
        common_prefix = strs[0]
        prefix_length = len(strs[0])
        str_idx = 1
        while str_idx < number_of_strings and prefix_length > 0:
            char_idx = 0
            string = strs[str_idx]
            string_length = len(string)
            while (char_idx < min([string_length, prefix_length])
                    and string[char_idx] == common_prefix[char_idx]):
                char_idx += 1
            common_prefix = common_prefix[:char_idx]
            prefix_length = len(common_prefix)
            str_idx += 1
        return common_prefix
