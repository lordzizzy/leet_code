# https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/596/week-4-april-22nd-april-28th/3723/

# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).


# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).


# Now consider if some obstacles are added to the grids. How many unique paths
# would there be?


# An obstacle and space is marked as 1 and 0 respectively in the grid.

# Example 1:
# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right

# Example 2:
# Input: obstacleGrid = [[0,1],[0,0]]
# Output: 1


# Constraints:
# m == obstacleGrid.length
# n == obstacleGrid[i].length
# 1 <= m, n <= 100
# obstacleGrid[i][j] is 0 or 1.

from typing import Callable, Deque, List, Set, Tuple
from termcolor import colored

from itertools import product

Matrix = List[List[int]]


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: Matrix) -> int:
        return self.uniquePathsWithObstacles_dfs_iterative(obstacleGrid)

    # this is the solution from leetcode, a little harder to understand because
    # it modifies obstacle grid inplace for the dp storage
    # i made some adjustments to the code to make it more pythonic
    # https://leetcode.com/problems/unique-paths-ii/solution/
    def uniquePathsWithObstacles_dp_inplace(self, obstacleGrid: Matrix) -> int:
        M = len(obstacleGrid)
        N = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0

        obstacleGrid[0][0] = 1

        # fill values for first column
        for i in range(1, M):
            obstacleGrid[i][0] = int(
                obstacleGrid[i][0] == 0 and obstacleGrid[i - 1][0] == 1
            )

        # fill values for first row
        for j in range(1, N):
            obstacleGrid[0][j] = int(
                obstacleGrid[0][j] == 0 and obstacleGrid[0][j - 1] == 1
            )

        # start from 1,1 and fill up values by summing cell from left and above
        for i, j in product(range(1, M), range(1, N)):
            if obstacleGrid[i][j] == 0:
                obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
            else:
                obstacleGrid[i][j] = 0

        return obstacleGrid[-1][-1]

    # this is an elegant dp implementation
    # https://leetcode.com/problems/unique-paths-ii/discuss/1180225/Python-short-dp-solution-explained
    def uniquePathsWithObstacles_dp_OMN_space(self, obstacleGrid: Matrix) -> int:
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * N for _ in range(M)]
        dp[0][0] = int(obstacleGrid[0][0] == 0)

        for i, j in product(range(M), range(N)):
            if obstacleGrid[i][j] == 1:
                continue
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]

        return dp[-1][-1]

    # this is the space optimization to O(N) space for the dp solution above
    # the idea is that each path will have to converge on each column from left
    # to right to reach the goal, so we only need N(col) spaces. brilliant.
    def uniquePathsWithObstacles_dp_ON_space(self, obstacleGrid: Matrix) -> int:
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        dp = [1] + [0] * N
        for i, j in product(range(M), range(N)):
            if obstacleGrid[i][j]:
                dp[j] = 0
            elif j > 0:
                dp[j] += dp[j - 1]
        return dp[-1]

    # my first attempt for a dfs solution
    # was too slow for leetcode, just document and learn
    def uniquePathsWithObstacles_dfs_iterative(self, obstacleGrid: Matrix) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0

        R = len(obstacleGrid)
        C = len(obstacleGrid[0])

        if R == 1 and C == 1:
            return 1

        start = (0, 0)
        goal = (R - 1, C - 1)
        moves = ((0, 1), (1, 0))

        open_nodes = Deque[Tuple[int, int]]()
        open_nodes.append(start)
        visited: Set[Tuple[int, int]] = set()

        res = 0

        while len(open_nodes):
            r, c = open_nodes.popleft()
            for dr, dc in moves:
                nr, nc = r + dr, c + dc
                if nr < R and nc < C:
                    if obstacleGrid[nr][nc] == 0:
                        if (nr, nc) == goal:
                            res += 1
                        elif (nr, nc) not in visited:
                            open_nodes.append((nr, nc))
            visited.add((r, c))

        return res


SolutionFunc = Callable[[Matrix], int]


def test_solution(obstacleGrid: Matrix, expected: int) -> None:
    def test_impl(func: SolutionFunc, obstacleGrid: Matrix, expected: int) -> None:
        r = func(obstacleGrid)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Num of unique paths in {obstacleGrid} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Num of unique paths in {obstacleGrid} is {r}, but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    obs_copy = [[c for c in r] for r in obstacleGrid]
    test_impl(sln.uniquePathsWithObstacles_dp_inplace, obs_copy, expected)
    test_impl(sln.uniquePathsWithObstacles_dfs_iterative, obstacleGrid, expected)


if __name__ == "__main__":
    test_solution(obstacleGrid=[[0]], expected=1)
    test_solution(obstacleGrid=[[0, 0, 0], [0, 1, 0], [0, 0, 0]], expected=2)
    test_solution(obstacleGrid=[[0, 1], [0, 0]], expected=1)
