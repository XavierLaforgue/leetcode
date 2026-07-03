from time import perf_counter_ns
from random import randint
from p0026__remove_duplicates_from_sorted_array import Solution


def create_input(n: int):
    nums = []
    element = randint(-100, 1)
    while len(nums) < n and element <= 100:
        duplicates = randint(1, 20)
        nums.extend([element] * duplicates)
        element += 1
    return nums[:n]


def benchmark(n: int = 30_000, repeats: int = 1000):
    sol = Solution()
    total = 0.0
    for _ in range(repeats):
        nums = create_input(n)
        start = perf_counter_ns()
        sol.removeDuplicates(nums)
        total += perf_counter_ns() - start

    print(f"avg: {(total / repeats) / 1000}us for nums.length={n}")


if __name__ == "__main__":
    benchmark()
