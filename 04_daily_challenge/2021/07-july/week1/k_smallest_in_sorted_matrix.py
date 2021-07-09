# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/608/week-1-july-1st-july-7th/3805/

# Kth Smallest Element in a Sorted Matrix

# Given an n x n matrix where each of the rows and columns are sorted in
# ascending order, return the kth smallest element in the matrix.

# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

# Example 1:
# Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
# Output: 13
# Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and
# the 8th smallest number is 13

# Example 2:
# Input: matrix = [[-5]], k = 1
# Output: -5

# Constraints:

# n == matrix.length
# n == matrix[i].length
# 1 <= n <= 300
# -10⁹ <= matrix[i][j] <= 10⁹
# All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
# 1 <= k <= n²

# reference
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/301357/Java-0ms-(added-Python-and-C%2B%2B)%3A-Easy-to-understand-solutions-using-Heap-and-Binary-Search

from bisect import bisect_right
from heapq import heappop, heappush
from typing import Callable, List, Tuple

from termcolor import colored


class Solution:
    # Time complexity: O(k logN)
    # Space complexity: O(N)
    def kthSmallest_heap(self, mat: List[List[int]], k: int) -> int:
        min_heap: List[Tuple[int, int, List[int]]] = []

        for i in range(min(k, len(mat))):
            heappush(min_heap, (mat[i][0], 0, mat[i]))

        num_cnt, num = 0, 0
        while min_heap:
            num, i, row = heappop(min_heap)
            num_cnt += 1
            if num_cnt == k:
                break
            if len(row) > i + 1:
                heappush(min_heap, (row[i + 1], i + 1, row))

        return num

    # Time complexity: O(N log(max-min))
    # Space complexity: O(1)
    def kthSmallest_binarysearch(self, mat: List[List[int]], k: int) -> int:
        lo, hi = mat[0][0], mat[-1][-1]

        while lo < hi:
            mid = (lo + hi) // 2

            if sum(bisect_right(row, mid) for row in mat) < k:
                lo = mid + 1
            else:
                hi = mid

        return lo


SolutionFunc = Callable[[List[List[int]], int], int]


def test_solution(matrix: List[List[int]], k: int, expected: int) -> None:
    def test_impl(
        func: SolutionFunc, matrix: List[List[int]], k: int, expected: int
    ) -> None:
        r = func(matrix, k)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => {k}th smallest num in {matrix} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => {k}th smallest num in {matrix} is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.kthSmallest_heap, matrix, k, expected)
    test_impl(sln.kthSmallest_binarysearch, matrix, k, expected)


if __name__ == "__main__":
    test_solution(matrix=[[1, 5, 9], [10, 11, 13], [12, 13, 15]], k=8, expected=13)
    test_solution(matrix=[[-5]], k=5, expected=-5)
