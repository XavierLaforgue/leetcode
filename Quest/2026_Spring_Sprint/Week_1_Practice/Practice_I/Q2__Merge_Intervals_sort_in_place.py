from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])
        clean_array = []
        for interval in intervals:
            if not clean_array:
                clean_array.append(interval)
                continue
            start = interval[0]
            end = interval[1]
            if start > clean_array[-1][1]:
                clean_array.append(interval)
                continue
            elif end > clean_array[-1][1]:
                clean_array[-1][1] = end
        return clean_array
