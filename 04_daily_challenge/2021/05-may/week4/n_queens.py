# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/601/week-4-may-22nd-may-28th/3752/

# N-Queens
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard
# such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle.

# Each solution contains a distinct board configuration of the n-queens'
# placement, where 'Q' and '.' both indicate a queen and an empty space,
# respectively.

# Example 1:
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as
# shown above

# Example 2:
# Input: n = 1
# Output: [["Q"]]

# Constraints:
# 1 <= n <= 9

from typing import Callable, List, Set
from termcolor import colored


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        return self.solveNQueens_backtrack(n)

    def solveNQueens_backtrack(self, n: int) -> List[List[str]]:
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

        return ans

    def solveNQueens_dfs(self, n: int) -> List[List[str]]:
        #TODO
        pass


SolutionFunc = Callable[[int], List[List[str]]]


def test_solution(n: int, expected: List[List[str]]) -> None:
    def test_impl(func: SolutionFunc, n: int, expected: List[List[str]]) -> None:
        r = func(n)
        if sorted(r) == sorted(expected):
            print(
                colored(
                    f"PASSED {func.__name__} => Solutions to {n}-Queens are {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Solutions to {n}-Queens are {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.solveNQueens_backtrack, n, expected)


if __name__ == "__main__":
    test_solution(
        n=4,
        expected=[[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]],
    )
    test_solution(n=1, expected=[["Q"]])
