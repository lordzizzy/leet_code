# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/608/week-1-july-1st-july-7th/3803/

# Reshape the Matrix
# In MATLAB, there is a handy function called reshape which can reshape an m x
# n matrix into a new one with a different size r x c keeping its original
# data.


# You are given an m x n matrix mat and two integers r and c representing the
# row number and column number of the wanted reshaped matrix.


# The reshaped matrix should be filled with all the elements of the original
# matrix in the same row-traversing order as they were.


# If the reshape operation with given parameters is possible and legal, output
# the new reshaped matrix; Otherwise, output the original matrix.


# Example 1:
# Input: mat = [[1,2],[3,4]], r = 1, c = 4
# Output: [[1,2,3,4]]

# Example 2:
# Input: mat = [[1,2],[3,4]], r = 2, c = 4
# Output: [[1,2],[3,4]]


# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 100
# -1000 <= mat[i][j] <= 1000
# 1 <= r, c <= 300

from typing import Callable, List

from termcolor import colored


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
        reshaped = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(r * c):
            reshaped[i // c][i % c] = mat[i // n][i % n]
        return reshaped


SolutionFunc = Callable[[List[List[int]], int, int], List[List[int]]]


def test_solution(
    mat: List[List[int]], r: int, c: int, expected: List[List[int]]
) -> None:
    def test_impl(
        func: SolutionFunc,
        mat: List[List[int]],
        r: int,
        c: int,
        expected: List[List[int]],
    ) -> None:
        res = func(mat, r, c)
        if res == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Reshaped matrix of {mat} is {res}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Reshaped matrix of {mat} is {res} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.matrixReshape, mat, r, c, expected)


if __name__ == "__main__":
    test_solution(mat=[[1, 2], [3, 4]], r=1, c=4, expected=[[1, 2, 3, 4]])
    test_solution(mat=[[1, 2], [3, 4]], r=2, c=4, expected=[[1, 2], [3, 4]])
