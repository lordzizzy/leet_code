# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/591/week-4-march-22nd-march-28th/3684/

# Pacific Atlantic Water Flow
# Given an m x n matrix of non-negative integers representing the height of
# each unit cell in a continent, the "Pacific ocean" touches the left and top
# edges of the matrix and the "Atlantic ocean" touches the right and bottom
# edges.

# Water can only flow in four directions (up, down, left, or right) from a cell
# to another one with height equal or lower.

# Find the list of grid coordinates where water can flow to both the Pacific
# and Atlantic ocean.

# Note:
# The order of returned grid coordinates does not matter.
# Both m and n are less than 150.

# Example:
# Given the following 5x5 matrix:
#   Pacific ~   ~   ~   ~   ~
#        ~  1   2   2   3  (5) *
#        ~  3   2   3  (4) (4) *
#        ~  2   4  (5)  3   1  *
#        ~ (6) (7)  1   4   5  *
#        ~ (5)  1   1   2   4  *
#           *   *   *   *   * Atlantic
# Return:
# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with
# parentheses in above matrix).

# Further explanation
# The matrix is the continent with water on it and the boundaries are the
# oceans. Left and top being Pacific and right and bottom being the Atlantic.
#
# The water on the continent (in the matrix) wants to flow out in the ocean.
# (Nature huh.)
#
# The numbers in the matrix is the height of the water for that point.
#
# For every point you have to ask the question. Can the water at this point and
# this height flow out in both the oceans under the constraints of flowing
# through only four(up, down, right, left) directions and flow into channels
# with same height or less height?
#
# If yes you return the coordinate of that point. Else you ignore it.
# To solidify this understanding, try to manually go to every point and see if
# the water can flow from there to both oceans or not.


from typing import Callable, Deque, List, Set, Tuple
from termcolor import colored


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        return self.pacificAtlantic_bfs(matrix)

    def pacificAtlantic_bfs(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []

        rows, cols = len(matrix), len(matrix[0])
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        pacific_q = Deque[Tuple[int, int]]()
        atlantic_q = Deque[Tuple[int, int]]()

        for i in range(rows):
            pacific_q.append((i, 0))
            atlantic_q.append((i, cols - 1))

        for i in range(cols):
            pacific_q.append((0, i))
            atlantic_q.append((rows - 1, i))

        def bfs(q: Deque[Tuple[int, int]]) -> Set[Tuple[int, int]]:
            reachable: Set[Tuple[int, int]] = set()
            while q:
                (r, c) = q.popleft()
                reachable.add((r, c))
                for (x, y) in dirs:
                    new_row, new_col = r + x, c + y
                    if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols:
                        continue
                    if (new_row, new_col) in reachable:
                        continue
                    if matrix[new_row][new_col] < matrix[r][c]:
                        continue
                    q.append((new_row, new_col))
            return reachable

        pac_reachable = bfs(pacific_q)
        atl_reachable = bfs(atlantic_q)

        s = pac_reachable.intersection(atl_reachable)

        return [[r, c] for r, c in s]


Matrix2D = List[List[int]]
SolutionFunc = Callable[[Matrix2D], Matrix2D]


def test_solution(matrix: Matrix2D, expected: Matrix2D) -> None:
    def test_impl(func: SolutionFunc, matrix: Matrix2D, expected: Matrix2D) -> None:
        r = func(matrix)
        if sorted(r) == sorted(expected):
            print(
                colored(
                    f"PASSED {func.__name__} => From {matrix}, the list of coordinates that can flow are {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => From {matrix}, the list of coordinates that can flow are {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.pacificAtlantic, matrix, expected)


if __name__ == "__main__":
    test_solution(
        matrix=[
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4],
        ],
        expected=[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]],
    )
