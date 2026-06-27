from typing import List


class Solution:

    def __init__(self):
        self.length = None

    def rob(self, nums: List[int]) -> int:
        number_of_houses = len(nums)
        if not self.length:
            self.cache = {0: 0}
            self.length = number_of_houses
        if number_of_houses in self.cache:
            return self.cache[number_of_houses]
        if number_of_houses == 1:
            self.cache[1] = nums[0]
            return self.cache[1]
        if number_of_houses == 2:
            self.cache[2] = max(nums)
            return self.cache[2]
        self.cache[number_of_houses] = max(
                nums[0] + self.rob(nums[2:]),
                nums[1] + self.rob(nums[3:])
                )
        return self.cache[number_of_houses]
