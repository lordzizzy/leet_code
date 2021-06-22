# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/605/week-3-june-15th-june-21st/3786/

# Pascal's Triangle
# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly
# above it as shown:

# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Example 2:
# Input: numRows = 1
# Output: [[1]]

# Constraints:
# 1 <= numRows <= 30

from typing import Callable, List
from termcolor import colored


class Solution:
    # Time complexity: O(N^2), Space complexity: O(N)
    def generate_dp_bottom_up(self, numRows: int) -> List[List[int]]:
        res: List[List[int]] = []

        for row_num in range(numRows):
            row = [0 for _ in range(row_num + 1)]
            row[0], row[-1] = 1, 1

            for j in range(1, len(row) - 1):
                row[j] = res[row_num - 1][j - 1] + res[row_num - 1][j]

            res.append(row)

        return res

    # reference:
    # https://leetcode.com/problems/pascals-triangle/discuss/38128/Python-4-lines-short-solution-using-map.
    #
    # Explanation: Any row can be constructed using the offset sum of the previous row.
    # Example:
    #     1 3 3 1 0
    #  +  0 1 3 3 1
    #  =  1 4 6 4 1
    def generate_dp_bottom_up2(self, numRows: int) -> List[List[int]]:
        res: List[List[int]] = [[1]]
        for _ in range(1, numRows):
            a, b = res[-1] + [0], [0] + res[-1]
            res.append([a[i] + b[i] for i in range(len(a))])
        return res[:numRows]


SolutionFunc = Callable[[int], List[List[int]]]


def test_solution(numRows: int, expected: List[List[int]]) -> None:
    def test_impl(func: SolutionFunc, numRows: int, expected: List[List[int]]) -> None:
        r = func(numRows)
        if len(r) == len(expected) and all(a == b for a, b in zip(r, expected)):
            print(
                colored(
                    f"PASSED {func.__name__} => Pascal's triangle of {numRows} rows is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Pascal's triangle of {numRows} rows is {r}, but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.generate_dp_bottom_up, numRows, expected)
    test_impl(sln.generate_dp_bottom_up2, numRows, expected)


if __name__ == "__main__":
    test_solution(
        numRows=5, expected=[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    )
    test_solution(numRows=1, expected=[[1]])
