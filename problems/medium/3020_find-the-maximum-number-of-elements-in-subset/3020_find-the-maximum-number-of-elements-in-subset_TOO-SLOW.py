from typing import List, Dict, TypedDict


class CacheEntry(TypedDict):
    # valid_set: List[int]
    maxL: int


class Solution:

    def __init__(self):
        self.cache: Dict[int, CacheEntry] = {}
        self.maxL = 1

    def helper(self, idx, nums: List[int]) -> int:
        num = nums[idx]
        num2 = num * num
        if num == 1:
            ones_in_nums = nums.count(1)
            maxL = ones_in_nums - (1 - ones_in_nums % 2)
            self.cache[1] = {
                # "valid_set": [1] * maxL,
                "maxL": maxL
            }
            return maxL
        if nums.count(num) == 1 or num2 not in nums:
            self.cache[num] = {
                # "valid_set": [num],
                "maxL": 1
            }
            return 1
        maxL = self.helper(nums.index(num2), nums)
        self.cache[num] = {
            # "valid_set": [num, *self.cache[num2]["valid_set"], num],
            "maxL": 2 + maxL
        }
        return self.cache[num]["maxL"]

    def maximumLength(self, nums: List[int]) -> int:
        for idx in range(len(nums)):
            if nums[idx] in self.cache:
                continue
            maxL = self.helper(idx, nums)
            if maxL > self.maxL:
                self.maxL = maxL
        return self.maxL
