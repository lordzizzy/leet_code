# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3638/

# Shortest Path in Binary Matrix
# In an N by N square grid, each cell is either empty (0) or blocked (1).

# A clear path from top-left to bottom-right has length k if and only if it is composed of cells C_1, C_2, ..., C_k such that:

# Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
# C_1 is at location (0, 0) (ie. has value grid[0][0])
# C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
# If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
# Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1.

# Example 1:
# Input: [[0,1],[1,0]]
# # Output: 2

# Example 2:
# Input: [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4

# Note:
# 1 <= grid.length == grid[0].length <= 100
# grid[r][c] is 0 or 1

from collections import deque
from typing import Callable, Deque, List, Set, Tuple
from termcolor import colored


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        return self.shortestPathBinaryMatrix_bfs(grid)

    def shortestPathBinaryMatrix_bfs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]:
            # no empty node
            return -1
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1))
        q: Deque[Tuple[int, int, int]] = deque([])
        q.append((0, 0, 1))
        visited: Set[Tuple[int, int]] = set()
        visited.add((0, 0))

        while len(q):
            r, c, dist = q.popleft()
            if r == n - 1 and c == n - 1:
                return dist
            for d1, d2 in dirs:
                x = r + d1
                y = c + d2
                if 0 <= x < n and 0 <= y < n:
                    if (x, y) not in visited and grid[x][y] == 0:
                        visited.add((x, y))
                        q.append((x, y, dist + 1))
        return -1


SolutionFunc = Callable[[List[List[int]]], int]


def test_solution(grid: List[List[int]], expected: int) -> None:
    def test_impl(func: SolutionFunc, grid: List[List[int]], expected: int) -> None:
        r = func(grid)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => {grid} shortest path thru is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"PASSED {func.__name__} => {grid} shortest path thru is {r}, but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.shortestPathBinaryMatrix_bfs, grid, expected)


if __name__ == "__main__":
    test_solution(grid=[[0, 1], [1, 0]], expected=2)
    test_solution(grid=[[0, 0, 0], [1, 1, 0], [1, 1, 0]], expected=4)
