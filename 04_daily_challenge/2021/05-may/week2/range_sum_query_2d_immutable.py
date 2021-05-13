# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/599/week-2-may-8th-may-14th/3740/

# Range Sum Query 2D - Immutable
# Given a 2D matrix matrix, handle multiple queries of the following type:

# Calculate the sum of the elements of matrix inside the rectangle defined by
# its upper left corner (row1, col1) and lower right corner (row2, col2).

# Implement the NumMatrix class:

# NumMatrix(int[][] matrix) Initializes the object with the integer matrix
# matrix.

#
# int sumRegion(int row1, int col1, int row2, int col2)
#
# Returns the sum of the elements of matrix inside the rectangle defined by its
# upper left corner (row1, col1) and lower right corner (row2, col2).


# Example 1:
# Input
# ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
# [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0,
# 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
# Output
# [null, 8, 11, 12]

# Explanation
# NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2,
# 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);

# numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
# numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
# numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)


# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 200
# -10⁵ <= matrix[i][j] <= 10⁵
# 0 <= row1 <= row2 < m
# 0 <= col1 <= col2 < n
# At most 10⁴ calls will be made to sumRegion.


from typing import List, Protocol
from termcolor import colored
from itertools import product
from functools import lru_cache

Matrix = List[List[int]]


class NumMatrix(Protocol):
    def __init__(self, matrix: Matrix):
        ...

    @lru_cache(maxsize=None)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ...


class NumMatrix_bruteforce_TLE(NumMatrix):
    def __init__(self, matrix: Matrix):
        self.m_ = matrix

    @lru_cache(maxsize=None)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        m = self.m_
        sum = 0
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                sum += m[i][j]
        return sum


class NumMatrix_cache_rows(NumMatrix):
    def __init__(self, matrix: Matrix):
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                dp[i][j + 1] = dp[i][j] + matrix[i][j]
        self.dp_ = dp

    @lru_cache(maxsize=None)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        dp = self.dp_
        for i in range(row1, row2 + 1):
            sum += dp[i][col2 + 1] - dp[i][col1]
        return sum


# SUM(ABCD) = SUM(OD) - SUM(OB) - SUM(OC) +  SUM(OA)
# O(1) time complexity, O(MN) memory
class NumMatrix_dp(NumMatrix):
    def __init__(self, matrix: Matrix):
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for j, i in product(range(n), range(m)):
            dp[i + 1][j + 1] = dp[i + 1][j] + dp[i][j + 1] - dp[i][j] + matrix[i][j]
        self.dp_ = dp

    @lru_cache(maxsize=None)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.dp_[row2 + 1][col2 + 1]
            - self.dp_[row1][col2 + 1]
            - self.dp_[row2 + 1][col1]
            + self.dp_[row1][col1]
        )


def test_solution(
    m: Matrix, row1: int, col1: int, row2: int, col2: int, expected: int
) -> None:
    def test_impl(
        nm: NumMatrix,
        row1: int,
        col1: int,
        row2: int,
        col2: int,
        expected: int,
    ) -> None:
        r = nm.sumRegion(row1, col1, row2, col2)
        if r == expected:
            print(
                colored(
                    f"PASSED {type(nm)} => Sum of region (({row1}, {col1}), ({row2, col2})) in {m} ",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {type(nm)} => Sum of region (({row1}, {col1}), ({row2, col2})) in {m} but expected {expected}",
                    "red",
                )
            )

    test_impl(
        nm=NumMatrix_bruteforce_TLE(m),
        row1=row1,
        col1=col1,
        row2=row2,
        col2=col2,
        expected=expected,
    )

    test_impl(
        nm=NumMatrix_cache_rows(m),
        row1=row1,
        col1=col1,
        row2=row2,
        col2=col2,
        expected=expected,
    )

    test_impl(
        nm=NumMatrix_dp(m),
        row1=row1,
        col1=col1,
        row2=row2,
        col2=col2,
        expected=expected,
    )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

M = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5],
]

if __name__ == "__main__":
    test_solution(m=M, row1=2, col1=1, row2=4, col2=3, expected=8)
    test_solution(m=M, row1=1, col1=1, row2=2, col2=2, expected=11)
    test_solution(m=M, row1=1, col1=2, row2=2, col2=4, expected=12)
