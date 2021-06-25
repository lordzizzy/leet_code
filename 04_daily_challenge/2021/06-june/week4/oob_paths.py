# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/606/week-4-june-22nd-june-28th/3790/

# Out of Boundary Paths

# There is an m x n grid with a ball. The ball is initially at the position
# [startRow, startColumn]. You are allowed to move the ball to one of the four
# adjacent four cells in the grid (possibly out of the grid crossing the grid
# boundary). You can apply at most maxMove moves to the ball.

# Given the five integers m, n, maxMove, startRow, startColumn, return the
# number of paths to move the ball out of the grid boundary. Since the answer
# can be very large, return it modulo 109 + 7.

# Example 1:
# Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
# Output: 6

# Example 2:
# Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
# Output: 12


# Constraints:
# 1 <= m, n <= 50
# 0 <= maxMove <= 50
# 0 <= startRow <= m
# 0 <= startColumn <= n

from functools import lru_cache
from typing import Callable

import numpy as np
from termcolor import colored


class Solution:
    # let N = number of moves allowed
    # Time complexity:  O(4^N)
    # Space complexity: O(N), depth of the recursion tree = N
    def findPaths_brute_force_recursive(
        self, m: int, n: int, maxMove: int, startRow: int, startCol: int
    ) -> int:
        MAX = int(1e9 + 7)

        def find_oob(moves: int, i: int, j: int) -> int:
            if i < 0 or i == m or j < 0 or j == n:
                return 1
            if moves == 0:
                return 0

            u = find_oob(moves - 1, i + 1, j) % MAX
            d = find_oob(moves - 1, i - 1, j) % MAX
            l = find_oob(moves - 1, i, j - 1) % MAX
            r = find_oob(moves - 1, i, j + 1) % MAX

            return (u + d + l + r) % MAX

        if maxMove == 0 and (
            startRow + maxMove < m
            or startRow - maxMove > 0
            or startCol + maxMove < n
            or startCol - maxMove > 0
        ):
            return 0

        return find_oob(maxMove, startRow, startCol) % MAX

    def findPaths_dp_topdown_memoization(
        self, m: int, n: int, maxMove: int, startRow: int, startCol: int
    ) -> int:
        MAX = int(1e9 + 7)
        memo = [[[-1] * (maxMove + 1) for _ in range(n)] for _ in range(m)]

        def find_oob(moves: int, i: int, j: int) -> int:
            if i < 0 or i == m or j < 0 or j == n:
                return 1
            if moves == 0:
                return 0

            if memo[i][j][moves] >= 0:
                return memo[i][j][moves]

            u = find_oob(moves - 1, i + 1, j) % MAX
            d = find_oob(moves - 1, i - 1, j) % MAX
            l = find_oob(moves - 1, i, j - 1) % MAX
            r = find_oob(moves - 1, i, j + 1) % MAX

            memo[i][j][moves] = (u + d + l + r) % MAX

            return memo[i][j][moves]

        if maxMove == 0 and (
            startRow + maxMove < m
            or startRow - maxMove > 0
            or startCol + maxMove < n
            or startCol - maxMove > 0
        ):
            return 0

        return find_oob(maxMove, startRow, startCol) % MAX

    # Surprisingly, using numpy in leetcode this way results in a much slower
    # time than normal python lists
    # 400+ms vs 100+ms
    # TODO: find out why
    def findPaths_dp_topdown_memoization_numpy(
        self, m: int, n: int, maxMove: int, startRow: int, startCol: int
    ) -> int:
        MAX = int(1e9 + 7)
        memo = np.full((m, n, maxMove + 1), -1, dtype="int64")

        def find_oob(moves: int, i: int, j: int) -> int:
            if i < 0 or i == m or j < 0 or j == n:
                return 1
            if moves == 0:
                return 0

            if memo[i][j][moves] >= 0:
                return memo[i][j][moves]

            u = find_oob(moves - 1, i + 1, j) % MAX
            d = find_oob(moves - 1, i - 1, j) % MAX
            l = find_oob(moves - 1, i, j - 1) % MAX
            r = find_oob(moves - 1, i, j + 1) % MAX

            memo[i][j][moves] = (u + d + l + r) % MAX

            return memo[i][j][moves]

        if maxMove == 0 and (
            startRow + maxMove < m
            or startRow - maxMove > 0
            or startCol + maxMove < n
            or startCol - maxMove > 0
        ):
            return 0

        return find_oob(maxMove, startRow, startCol) % MAX

    def findPaths_dp_topdown_memoization_lrucache(
        self, m: int, n: int, maxMove: int, startRow: int, startCol: int
    ) -> int:
        MAX = int(1e9 + 7)

        @lru_cache(maxsize=None)
        def find_oob(moves: int, i: int, j: int) -> int:
            if i < 0 or i == m or j < 0 or j == n:
                return 1
            if moves == 0:
                return 0

            u = find_oob(moves - 1, i + 1, j) % MAX
            d = find_oob(moves - 1, i - 1, j) % MAX
            l = find_oob(moves - 1, i, j - 1) % MAX
            r = find_oob(moves - 1, i, j + 1) % MAX

            return (u + d + l + r) % MAX

        return find_oob(maxMove, startRow, startCol) % MAX


SolutionFunc = Callable[[int, int, int, int, int], int]


def test_solution(
    m: int, n: int, maxMove: int, startRow: int, startColumn: int, expected: int
) -> None:
    def test_impl(
        func: SolutionFunc,
        m: int,
        n: int,
        maxMove: int,
        startRow: int,
        startColumn: int,
        expected: int,
    ) -> None:
        r = func(m, n, maxMove, startRow, startColumn)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Number of paths to make ball go OOB for grid {m}x{n}, maxMoves={maxMove}, start:({startRow},{startColumn}) is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Number of paths to make ball go OOB for grid {m}x{n}, maxMoves={maxMove}, start:({startRow},{startColumn}) is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(
        sln.findPaths_brute_force_recursive,
        m,
        n,
        maxMove,
        startRow,
        startColumn,
        expected,
    )

    test_impl(
        sln.findPaths_dp_topdown_memoization,
        m,
        n,
        maxMove,
        startRow,
        startColumn,
        expected,
    )

    test_impl(
        sln.findPaths_dp_topdown_memoization_numpy,
        m,
        n,
        maxMove,
        startRow,
        startColumn,
        expected,
    )

    test_impl(
        sln.findPaths_dp_topdown_memoization_lrucache,
        m,
        n,
        maxMove,
        startRow,
        startColumn,
        expected,
    )


if __name__ == "__main__":
    test_solution(m=2, n=2, maxMove=2, startRow=0, startColumn=0, expected=6)
    test_solution(m=1, n=3, maxMove=3, startRow=0, startColumn=1, expected=12)
    test_solution(m=10, n=5, maxMove=10, startRow=2, startColumn=3, expected=65396)

    # murders bruteforce approach
    # test_solution(m=35, n=5, maxMove=50, startRow=15, startColumn=3, expected=489927958)
