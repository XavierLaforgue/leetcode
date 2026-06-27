from typing import List, Dict
from collections import Counter


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        freq_map: Dict[int, int] = Counter(nums)

        maxL = 0
        for num in freq_map.keys():
            if num == 1:
                current = freq_map[1] if freq_map[1] % 2 else freq_map[1] - 1
            else:
                current = 0
                num2 = num * num
                while freq_map[num] > 1 and num2 in freq_map:
                    current += 2
                    num = num2
                    num2 = num2 * num2
                current += 1
            maxL = max(maxL, current)
        return maxL
