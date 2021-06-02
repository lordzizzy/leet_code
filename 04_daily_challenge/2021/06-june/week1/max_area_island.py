# https://leetcode.com/explore/featured/card/june-leetcoding-challenge-2021/603/week-1-june-1st-june-7th/3764/

# Max Area of Island
# You are given an m x n binary matrix grid. An island is a group of 1's
# (representing land) connected 4-directionally (horizontal or vertical.) You
# may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return
# 0.

# Example 1:
# Input: grid =
# [
#     [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
#     [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
#     [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
# ]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected
# 4-directionally.

# Example 2:
# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0

# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] is either 0 or 1.

from typing import Callable, List, Set, Tuple
from termcolor import colored
from itertools import product


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        return self.maxAreaOfIsland_dfs_recursive(grid)

    def maxAreaOfIsland_dfs_recursive(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        seen: Set[Tuple[int, int]] = set()

        def area(r: int, c: int) -> int:
            if not (0 <= r < M and 0 <= c < N and (r, c) not in seen and grid[r][c]):
                return 0
            seen.add((r, c))
            return 1 + area(r + 1, c) + area(r - 1, c) + area(r, c + 1) + area(r, c - 1)

        return max(area(r, c) for r in range(M) for c in range(N))

    def maxAreaOfIsland_dfs_iterative(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        seen: Set[Tuple[int, int]] = set()
        ans = 0

        for row, col in product(range(M), range(N)):
            if grid[row][col] == 0 or (row, col) in seen:
                continue
            stack = [(row, col)]
            seen.add((row, col))
            area = 0
            while len(stack):
                r, c = stack.pop()
                area += 1
                for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if (
                        0 <= nr < M
                        and 0 <= nc < N
                        and (nr, nc) not in seen
                        and grid[nr][nc]
                    ):
                        stack.append((nr, nc))
                        seen.add((nr, nc))
            ans = max(ans, area)

        return ans


SolutionFunc = Callable[[List[List[int]]], int]


def test_solution(grid: List[List[int]], expected: int) -> None:
    def test_impl(func: SolutionFunc, grid: List[List[int]], expected: int) -> None:
        r = func(grid)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Max area of island with grid {grid} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Max area of island with grid {grid} is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.maxAreaOfIsland_dfs_recursive, grid, expected)
    test_impl(sln.maxAreaOfIsland_dfs_iterative, grid, expected)


if __name__ == "__main__":
    test_solution(
        grid=[
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        ],
        expected=6,
    )

    test_solution(grid=[[0, 0, 0, 0, 0, 0, 0, 0]], expected=0)
