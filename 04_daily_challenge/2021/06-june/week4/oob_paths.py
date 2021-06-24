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

from typing import Callable

from termcolor import colored


class Solution:
    # let N = number of moves allowed
    # Time complexity:  O(4^N)
    # Space complexity: O(N), depth of the recursion tree = N
    def findPaths_brute_force_recursive(
        self, m: int, n: int, maxMove: int, startRow: int, startCol: int
    ) -> int:
        def find_oob(maxMove: int, startRow: int, startCol: int) -> int:
            if startRow < 0 or startRow == m or startCol < 0 or startCol == n:
                return 1
            if maxMove == 0:
                return 0
            return (
                find_oob(maxMove - 1, startRow - 1, startCol)
                + find_oob(maxMove - 1, startRow + 1, startCol)
                + find_oob(maxMove - 1, startRow, startCol - 1)
                + find_oob(maxMove - 1, startRow, startCol + 1)
            )

        if maxMove == 0 and (
            startRow + maxMove < m
            or startRow - maxMove > 0
            or startCol + maxMove < n
            or startCol - maxMove > 0
        ):
            return 0

        return find_oob(maxMove, startRow, startCol) % int(1e9 + 7)


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


if __name__ == "__main__":
    test_solution(m=2, n=2, maxMove=2, startRow=0, startColumn=0, expected=6)
    test_solution(m=1, n=3, maxMove=3, startRow=0, startColumn=1, expected=12)
