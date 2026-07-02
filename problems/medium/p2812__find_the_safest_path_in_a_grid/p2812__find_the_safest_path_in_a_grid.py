from collections import deque
from threading import local


class Solution:

    @staticmethod
    def create_thief_queue_and_grid(grid: list[list[int]])\
            -> tuple[list[list[int]], deque]:
        thief_queue = deque()
        thief_grid = []
        for row_number, row in enumerate(grid):
            thief_grid.append([])
            for elem_number, elem in enumerate(row):
                if elem == 1:
                    thief_queue.append((row_number, elem_number))
                    thief_grid[row_number].append(0)
                else:
                    thief_grid[row_number].append(-1)
        return thief_grid, thief_queue

    @staticmethod
    def get_neighbours(x: int, y: int, size: int) -> list[tuple]:
        neighbours = []
        right = x + 1
        left = x - 1
        up = y + 1
        down = y - 1
        if right < size:
            neighbours.append((right, y))
        if left >= 0:
            neighbours.append((left, y))
        if up < size:
            neighbours.append((x, up))
        if down >= 0:
            neighbours.append((x, down))
        return neighbours

    @staticmethod
    def get_safeness_per_cell(grid: list[list[int]], grid_size: int) -> list[list[int]]:
        safeness_grid, visit_queue = Solution.create_thief_queue_and_grid(grid)
        while visit_queue:
            row_num, elem_num = visit_queue.pop()
            local_safeness = safeness_grid[row_num][elem_num]
            neighbours = Solution.get_neighbours(row_num, elem_num, grid_size)
            for row_num, elem_num in neighbours:
                if safeness_grid[row_num][elem_num] == -1:
                    safeness_grid[row_num][elem_num] = local_safeness + 1
                    visit_queue.appendleft((row_num, elem_num))
        return safeness_grid

    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:
        grid_size = len(grid)
        safeness_grid = Solution.get_safeness_per_cell(grid, grid_size)
        return 0
