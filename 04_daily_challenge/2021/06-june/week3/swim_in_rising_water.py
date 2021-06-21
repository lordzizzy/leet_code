# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/605/week-3-june-15th-june-21st/3785/

# Swim in Rising Water
# On an N x N grid, each square grid[i][j] represents the elevation at that point (i,j).

# Now rain starts to fall. At time t, the depth of the water everywhere is t.
# You can swim from a square to another 4-directionally adjacent square if and
# only if the elevation of both squares individually are at most t. You can
# swim infinite distance in zero time. Of course, you must stay within the
# boundaries of the grid during your swim.

# You start at the top left square (0, 0). What is the least time until you can
# reach the bottom right square (N-1, N-1)?


# Example 1:
# Input: [[0,2],[1,3]]
# Output: 3
# Explanation:
# At time 0, you are in grid location (0, 0).
# You cannot go anywhere else because 4-directionally adjacent neighbors have a
# higher elevation than t = 0.
# You cannot reach point (1, 1) until time 3.
# When the depth of water is 3, we can swim anywhere inside the grid.

# Example 2:
# Input:
# [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
# Output: 16
# Explanation:
#  0  1  2  3  4
# 24 23 22 21  5
# 12 13 14 15 16
# 11 17 18 19 20
# 10  9  8  7  6

# The final route is marked in bold.
# We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
# Note:

# 2 <= N <= 50.
# grid[i][j] is a permutation of [0, ..., N*N - 1].

import heapq
from typing import Callable, List

from termcolor import colored


class Solution:
    def swimInWater_priority_q(self, grid: List[List[int]]) -> int:
        N = len(grid)
        pq = [(grid[0][0], 0, 0)]
        seen = set([(0, 0)])
        res = 0

        while pq:
            T, x, y = heapq.heappop(pq)
            res = max(res, T)
            if x == y == N - 1:
                return res
            for i, j in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
                if 0 <= i < N and 0 <= j < N and (i, j) not in seen:
                    seen.add((i, j))
                    heapq.heappush(pq, (grid[i][j], i, j))

        return res


SolutionFunc = Callable[[List[List[int]]], int]


def test_solution(grid: List[List[int]], expected: int) -> None:
    def test_impl(func: SolutionFunc, grid: List[List[int]], expected: int) -> None:
        r = func(grid)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Least time to reach bottom right square for {grid} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Least time to reach bottom right square for {grid} is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.swimInWater_priority_q, grid, expected)


if __name__ == "__main__":
    test_solution(grid=[[0, 2], [1, 3]], expected=3)
    test_solution(
        grid=[
            [0, 1, 2, 3, 4],
            [24, 23, 22, 21, 5],
            [12, 13, 14, 15, 16],
            [11, 17, 18, 19, 20],
            [10, 9, 8, 7, 6],
        ],
        expected=16,
    )
