# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3614/

# A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

# Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.

# Example 1:
# Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
# Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]

# Constraints:
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 100
# 1 <= mat[i][j] <= 100

# sample 64 ms solution
# class Solution:
#     def diagonalSort(self, A: List[List[int]]) -> List[List[int]]:
#         n, m = len(A), len(A[0])
#         d = collections.defaultdict(list)
#         for i in range(n):
#             for j in range(m):
#                 d[i - j].append(A[i][j])
#         for k in d:
#             d[k].sort(reverse=1)
#         for i in range(n):
#             for j in range(m):
#                 A[i][j] = d[i - j].pop()
#         return A

from termcolor import colored
from typing import List
from collections import defaultdict

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n, d = len(mat), len(mat[0]), defaultdict(list)

        # foreach number in diagonal "j-i", append to list with the key value j-i
        for i in range(m):
            for j in range (n):
                d[j - i].append(mat[i][j])

        # sort each list in diagonal and populate back to mat to sort it
        for k in d:
            for i, num in enumerate(sorted(d[k])):
                # print(f"diagonal {k}")
                # print(f"mat[{i} + max(-{k}, 0)][{k} + {i} + max(-{k}, 0)] = {num}")
                mat[i + max(-k, 0)][k + i + max(-k, 0)] = num

        return mat


def test_Solution(mat: List[List[int]], expected: List[List[int]]):
    sln = Solution()
    r = sln.diagonalSort(mat)
    if r == expected:
        print(colored(f"PASSED - Diagonal sort of mat {mat} is {r}", "green"))
    else:
        print(colored(f"FAILED - Diagonal sort of mat {mat} is {r}, but expected: {expected}", "red"))


if __name__ == "__main__":
    test_Solution(mat=[[3, 3, 1, 1],
                       [2, 2, 1, 2],
                       [1, 1, 1, 2]],
                  expected=[[1, 1, 1, 1],
                            [1, 2, 2, 2],
                            [1, 2, 3, 3]])
