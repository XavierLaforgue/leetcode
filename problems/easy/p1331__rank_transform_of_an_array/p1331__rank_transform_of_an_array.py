class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        sorted_arr = sorted(set(arr))
        ranked_dict = {}
        for rank, elem in enumerate(sorted_arr, 1):
            ranked_dict[elem] = rank
        return [ranked_dict[elem] for elem in arr]
