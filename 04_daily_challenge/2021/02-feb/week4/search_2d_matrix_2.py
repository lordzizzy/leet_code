# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/587/week-4-february-22nd-february-28th/3650/

# Search a 2D Matrix II
# Write an efficient algorithm that searches for a target value in an m x n
# integer matrix. The matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.

# Example 1:
# Input: matrix =
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
# target = 5
# Output: true

# Example 2:
# Input: matrix =
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
# target = 20
# Output: false

# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= n, m <= 300
# -10⁹ <= matix[i][j] <= 10⁹
# All the integers in each row are sorted in ascending order.
# All the integers in each column are sorted in ascending order.
# -10⁹ <= target <= 10⁹

from typing import Callable, List
from termcolor import colored

Matrix = List[List[int]]


class Solution:
    def searchMatrix(self, matrix: Matrix, target: int) -> bool:
        return self.searchMatrix_bin_search(matrix, target)

    # put == check at the last branch to help branch prediction since most of
    # the time the == will be passed
    def searchMatrix_topright_m_plus_n(self, matrix: Matrix, target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        r, c = 0, n - 1
        while r < m and c >= 0:
            cur = matrix[r][c]
            if cur < target:
                r += 1
            elif cur > target:
                c -= 1
            else:
                return True
        return False

    def searchMatrix_bin_search(self, matrix: Matrix, target: int) -> bool:
        def binary_search(target: int, arr: List[int], low: int, high: int) -> int:
            if low > high:
                return -1
            mid = (low + high) // 2
            if target < arr[mid]:
                return binary_search(target, arr, low, mid - 1)
            elif target > arr[mid]:
                return binary_search(target, arr, mid + 1, high)
            else:
                return mid

        for row in matrix:
            if row[0] <= target <= row[-1]:
                if binary_search(target, row, 0, len(row)) > -1:
                    return True

        return False


SolutionFunc = Callable[[List[List[int]], int], bool]


def test_solution(matrix: Matrix, target: int, expected: bool) -> None:
    def test_impl(
        func: SolutionFunc, matrix: Matrix, target: int, expected: bool
    ) -> None:
        r = func(matrix, target)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => {target} found in {matrix} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => {target} found in {matrix} is {r}, but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.searchMatrix_topright_m_plus_n, matrix, target, expected)
    test_impl(sln.searchMatrix_bin_search, matrix, target, expected)


if __name__ == "__main__":
    test_solution(
        matrix=[
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30],
        ],
        target=18,
        expected=True,
    )

    test_solution(
        matrix=[
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30],
        ],
        target=20,
        expected=False,
    )
