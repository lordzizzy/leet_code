# https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/596/week-4-april-22nd-april-28th/3720/

# Rotate Image
# You are given an n x n 2D matrix representing an image, rotate the image by
# 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the
# input 2D matrix directly. DO NOT allocate another 2D matrix and do the
# rotation.
#

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

# Example 2:
# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

# Example 3:
# Input: matrix = [[1]]
# Output: [[1]]

# Example 4:
# Input: matrix = [[1,2],[3,4]]
# Output: [[3,1],[4,2]]


# Constraints:
# matrix.length == n
# matrix[i].length == n
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000

# https://leetcode.com/problems/rotate-image/solution/
# https://leetcode.com/problems/rotate-image/discuss/18872/A-common-method-to-rotate-the-image
# https://leetcode.com/problems/rotate-image/discuss/18884/Seven-Short-Solutions-(1-to-7-lines)

from typing import Callable, List
from termcolor import colored

Matrix = List[List[int]]


class Solution:
    def rotate(self, m: Matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        return self.rotate_reverse_then_swap(m)

    def rotate_reverse_then_swap(self, m: Matrix) -> None:
        N = len(m)
        m.reverse()
        for i in range(N):
            for j in range(i + 1, N):
                m[i][j], m[j][i] = m[j][i], m[i][j]


SolutionFunc = Callable[[Matrix], None]


def test_solution(matrix: Matrix, expected: Matrix) -> None:
    def test_impl(func: SolutionFunc, matrix: Matrix, expected: Matrix) -> None:
        m = [r.copy() for r in matrix]
        func(matrix)
        if len(matrix) == len(expected) and all(
            r1 == r2 for r1, r2 in zip(matrix, expected)
        ):
            print(
                colored(f"PASSED {func.__name__} => {m} rotated is {matrix}", "green")
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => {m} rotated is {matrix}, but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.rotate, matrix, expected)


if __name__ == "__main__":
    test_solution(
        matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        expected=[[7, 4, 1], [8, 5, 2], [9, 6, 3]],
    )
    test_solution(
        matrix=[[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
        expected=[[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]],
    )
