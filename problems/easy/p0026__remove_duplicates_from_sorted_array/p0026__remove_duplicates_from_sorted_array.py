class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        length = len(nums)
        if length == 1:
            return 1
        pos = 0
        for num in nums[1:]:
            if num != nums[pos]:
                pos += 1
                nums[pos] = num
        return pos + 1
