# https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/595/week-3-april-15th-april-21st/3715/

# Triangle
# Given a triangle array, return the minimum path sum from top to bottom.

# For each step, you may move to an adjacent number of the row below. More
# formally, if you are on index i on the current row, you may move to either
# index i or index i + 1 on the next row.

# Example 1:
# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined
# above).

# Example 2:
# Input: triangle = [[-10]]
# Output: -10

# Constraints:

# 1 <= triangle.length <= 200
# triangle[0].length == 1
# triangle[i].length == triangle[i - 1].length + 1
# -10⁴ <= triangle[i][j] <= 10⁴

# Follow up: Could you do this using only O(n) extra space, where n is the
# total number of rows in the triangle?

# https://leetcode.com/problems/triangle/solution/

from typing import Callable, List
from termcolor import colored
from functools import lru_cache


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return self.minimumTotal_dp_bottomup_inplace(triangle)

    def minimumTotal_dp_bottomup_inplace(self, triangle: List[List[int]]) -> int:
        for row in range(1, len(triangle)):
            for col in range(row + 1):
                smallest_above = int(1e4)
                if col > 0:
                    smallest_above = triangle[row - 1][col - 1]
                if col < row:
                    smallest_above = min(smallest_above, triangle[row - 1][col])
                triangle[row][col] += smallest_above
        return min(triangle[-1])

    def minimumTotal_dp_bottomup_auxillaryspace(self, triangle: List[List[int]]) -> int:
        prev_row = triangle[0]
        for row in range(1, len(triangle)):
            curr_row: List[int] = []
            for col in range(row + 1):
                smallest_above = int(1e4)
                if col > 0:
                    smallest_above = prev_row[col - 1]
                if col < row:
                    smallest_above = min(smallest_above, prev_row[col])
                curr_row.append(triangle[row][col] + smallest_above)
            prev_row = curr_row
        return min(prev_row)

    def minimumTotal_dp_bottomup_flipped_auxillaryspace(
        self, triangle: List[List[int]]
    ) -> int:
        below_row = triangle[-1]
        n = len(triangle)
        for row in reversed(range(n - 1)):
            curr_row: List[int] = []
            for col in range(row + 1):
                smallest_below = min(below_row[col], below_row[col + 1])
                curr_row.append(triangle[row][col] + smallest_below)
            below_row = curr_row
        return below_row[0]

    def minimumTotal_dp_topdown_memoization(self, triangle: List[List[int]]) -> int:
        @lru_cache(maxsize=None)
        def min_path(row: int, col: int) -> int:
            path = triangle[row][col]
            if row < len(triangle) - 1:
                path += min(min_path(row + 1, col), min_path(row + 1, col + 1))
            return path

        return min_path(0, 0)


SolutionFunc = Callable[[List[List[int]]], int]


def test_solution(triangle: List[List[int]], expected: int) -> None:
    def test_impl(func: SolutionFunc, triangle: List[List[int]], expected: int) -> None:
        r = func(triangle)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Min sum path for triangle {triangle} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Min sum path for triangle {triangle} is {r}, but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.minimumTotal_dp_bottomup_auxillaryspace, triangle, expected)
    test_impl(sln.minimumTotal_dp_bottomup_flipped_auxillaryspace, triangle, expected)


if __name__ == "__main__":
    test_solution(triangle=[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]], expected=11)
    test_solution(triangle=[[-10]], expected=-10)
