# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/602/week-5-may-29th-may-31st/3760/

# The n-queens puzzle is the problem of placing n queens on an n x n chessboard
# such that no two queens attack each other.

# Given an integer n, return the number of distinct solutions to the n-queens
# puzzle.

# Example 1:
# Input: n = 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as
# shown.

# Example 2:
# Input: n = 1
# Output: 1

# Constraints:
# 1 <= n <= 9

from typing import Callable, List, Set
from termcolor import colored


class Solution:
    def totalNQueens(self, n: int) -> int:
        return self.totalNQueens_backtrack(n)

    def totalNQueens_backtrack(self, n: int) -> int:
        def create_board(state: List[List[str]]) -> List[str]:
            return ["".join(row) for row in state]

        def backtrack(row: int) -> None:
            # base case - N queens have been placed
            if row == n:
                ans.append(create_board(state))
                return

            for col in range(n):
                d, ad = row - col, row + col
                if col in cols or d in diags or ad in anti_diags:
                    continue
                # add queen
                cols.add(col)
                diags.add(d)
                anti_diags.add(ad)
                state[row][col] = "Q"

                backtrack(row + 1)

                # remove the queen from the board since we have already
                # explored all valid paths using the above function call
                cols.remove(col)
                diags.remove(d)
                anti_diags.remove(ad)
                state[row][col] = "."

        ans: List[List[str]] = []
        cols: Set[int] = set()
        diags: Set[int] = set()
        anti_diags: Set[int] = set()
        state: List[List[str]] = [["."] * n for _ in range(n)]

        backtrack(0)

        return len(ans)


SolutionFunc = Callable[[int], int]


def test_solution(n: int, expected: int) -> None:
    def test_impl(func: SolutionFunc, n: int, expected: int) -> None:
        r = func(n)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Total number of solutions to {n}-queens is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Total number of solutions to {n}-queens is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.totalNQueens_backtrack, n, expected)


if __name__ == "__main__":
    test_solution(n=1, expected=1)
