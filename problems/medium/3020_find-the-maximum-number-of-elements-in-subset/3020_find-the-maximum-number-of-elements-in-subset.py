from typing import List, Dict


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        freq_map: Dict[int, int] = {}
        maxL_map: Dict[int, int] = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
        maxL: int = (
            1 if 1 not in freq_map else
            freq_map[1] if freq_map[1] % 2 else freq_map[1] - 1
        )

        def helper(num: int) -> int:
            if num in maxL_map:
                return maxL_map[num]
            num2 = num * num
            if freq_map[num] == 1 or num2 not in freq_map:
                maxL_map[num] = 1
                return 1
            maxL_map[num] = 2 + helper(num2)
            return maxL_map[num]

        for num in freq_map:
            if num == 1:
                continue
            maxL = max(maxL, helper(num))
        return maxL
