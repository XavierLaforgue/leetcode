class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        sorted_arr = sorted(arr)
        rank = 1
        ranked_dict = {}
        for elem in sorted_arr:
            if elem not in ranked_dict:
                ranked_dict[elem] = rank
                rank += 1
        return [ranked_dict[elem] for elem in arr]



        ## ------  TOO SLOW  --------------
        # if not arr:
        #     return []
        # ranked_arr = []
        # rank0 = -1
        # for elem in arr:
        #     last = 1
        #     for rank0 in range(len(ranked_arr)):
        #         if elem <= ranked_arr[rank0]:
        #             last = 0
        #             break
        #     if rank0 != -1 and elem == ranked_arr[rank0]:
        #         continue
        #     ranked_arr.insert(rank0 + last, elem)
        # return [ranked_arr.index(elem) + 1 for elem in arr]
